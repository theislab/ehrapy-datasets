from database_processing.timeseriesprocessor import TimeseriesProcessor


class hiridTSP(TimeseriesProcessor):
    """
    Our processing of the hirid database handles 
    * 2 long tables: timeseries and pharma
    * 1 medication table that was computed in 1_hirid.py
    """
    def __init__(self, ts, pharma):
        super().__init__(dataset='hirid')
        self.lf_ts = (self.scan(self.savepath+ts)
                      .select('admissionid',
                              'variable',
                              'value',
                              self.col_offset))
        self.lf_med = self.scan(self.savepath+pharma)

        self.med_colnames = {'col_id': 'admissionid',
                             'col_var': 'label'}

        self.ts_colnames = {'col_id': 'admissionid',
                            'col_var': 'variable',
                            'col_value': 'value',
                            'col_time': self.col_offset}

        self.loadcols = self.ts_colnames.values()

    def _get_stays(self):
        stays = self.scan(self.labels_savepath).select('admissionid').unique().collect().to_numpy().flatten()
        return stays
    
    
    def run_harmonization(self):
        kept_variables = (self.kept_ts+['Body weight', 'Body height measure'])

        lf_ts = self.harmonize_columns(self.lf_ts, **self.ts_colnames)
        lf_med = self.harmonize_columns(self.lf_med, **self.med_colnames)

        lf_ts = self.filter_tables(lf_ts, kept_variables=kept_variables)
        lf_med = self.filter_tables(lf_med, kept_variables=self.kept_med)
    
        self.timeseries_to_long(lf_ts, sink=False)
        self.medication_to_long(lf_med)
        
        
    def run_preprocessing(self, reset_dir=None):
        raise UserWarning("This function is not maintained. It should be replaced"
                          "by a cleaner/faster alternative in the future.\n"
                          "Contributions welcome.")
        self.reset_dir(reset_dir)

        kept_variables = (self.kept_ts+['Body weight', 'Body height measure'])

        lf_ts = self.harmonize_columns(self.lf_ts, **self.ts_colnames)
        lf_med = self.harmonize_columns(self.lf_med, **self.med_colnames)

        lf_ts = self.filter_tables(lf_ts, kept_variables=kept_variables)
        lf_med = self.filter_tables(lf_med, kept_variables=self.kept_med)

        self.stays = self._get_stays()
        self.stay_chunks = self.get_stay_chunks()

        for chunk_number, stay_chunk in enumerate(self.stay_chunks):
            print(f'Chunk {chunk_number}')

            self.ts = (self.filter_tables(lf_ts,
                                    kept_variables=kept_variables,
                                    kept_stays=stay_chunk)
                       .collect(streaming=True))

            self.med = (self.filter_tables(lf_med,
                                    kept_variables=self.kept_med,
                                     kept_stays=stay_chunk))
            
            lf_formatted_ts = self.pl_format_raw_data(self.ts.lazy(), med=self.med, chunk_number=chunk_number)

            self.newprocess_tables(lf_formatted_ts.to_pandas(), med=self.med.collect().to_pandas(), chunk_number=chunk_number)
