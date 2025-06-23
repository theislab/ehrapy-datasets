from pathlib import Path

import pandas as pd


def convert_to_parquet(pth_dic):
    '''
    Writes larger csv files to parquet for faster access.
    Does not proceed if target files already exist.
    '''
    pth_voc = Path(pth_dic['vocabulary'])
    source_pth_concept = pth_voc / 'CONCEPT.csv'
    source_pth_concept_relationship = pth_voc / 'CONCEPT_RELATIONSHIP.csv'
    target_pth_concept = pth_voc / 'CONCEPT.parquet'
    target_pth_concept_relationship = pth_voc / 'CONCEPT_RELATIONSHIP.parquet'
    
    if not target_pth_concept.is_file():
        print(f'Loading {source_pth_concept}')
        df = pd.read_csv(source_pth_concept,
                         sep='\t',
                         index_col='concept_id')
        df.astype({'concept_code': str}).to_parquet(target_pth_concept)
        print(f' --> Saved {target_pth_concept}')
    if not target_pth_concept_relationship.is_file():
        print(f'Loading {source_pth_concept_relationship}')
        df = pd.read_csv(source_pth_concept_relationship,
                         sep='\t')
        df.to_parquet(target_pth_concept_relationship)
        print(f' --> Saved {target_pth_concept_relationship}')
