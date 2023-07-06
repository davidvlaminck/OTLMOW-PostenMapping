from pathlib import Path
from pathlib import Path
from typing import Optional

import sqlalchemy
from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from otlmow_postenmapping.TypeTemplateORM.Base import Base
from otlmow_postenmapping.TypeTemplateORM.GeneralInfo import Info
from otlmow_postenmapping.TypeTemplateORM.TemplateMapping import TemplateMapping


class MappingConverter:
    def __init__(self, db_path: Optional[Path] = None):
        self.db_engine = self.return_engine_using_path(db_path)
        with self.db_engine.connect() as conn:
            Base.metadata.create_all(conn)

    def convert(self, mapping: dict):
        with Session(self.db_engine) as session:
            session.connection()

            for k, v in mapping.items():
                if k == 'version':
                    session.execute(
                        insert(Info),
                        [{'parameter': 'Version', 'waarde': mapping['version']}]
                    )
                    session.commit()
                else:
                    template_name = k
                    row_number = 0
                    for asset_name, asset_dict in v.items():
                        for attribuut, attribuut_dict in asset_dict['attributen'].items():
                            row_number += 1
                            template_mapping = TemplateMapping()
                            template_mapping.standaardpostnummer = template_name
                            template_mapping.tempID = asset_name
                            template_mapping.isHoofdAsset = asset_dict['isHoofdAsset']
                            template_mapping.typeURI = asset_dict['typeURI']
                            template_mapping.rijNummer = row_number
                            template_mapping.dotnotatie = attribuut_dict['dotnotation']
                            template_mapping.attribuutURI = attribuut_dict['typeURI']
                            template_mapping.defaultWaarde = attribuut_dict['value']
                            session.add(template_mapping)
                            session.commit()

    def get_version(self) -> str:
        with Session(self.db_engine) as session:
            info_version = session.scalars(select(Info).where(Info.parameter == 'Version')).first()
            return info_version.waarde

    @staticmethod
    def return_engine_using_path(db_path: Optional[Path] = None) -> sqlalchemy.engine.base.Engine:
        if db_path is None:
            return sqlalchemy.create_engine(f'sqlite://')
        else:
            return sqlalchemy.create_engine(f'sqlite:////{db_path.absolute()}')

    def get_template_rows_by_name(self, template_name: str) -> list:
        with Session(self.db_engine) as session:
            stmt = select(TemplateMapping).\
                where(TemplateMapping.standaardpostnummer == template_name).\
                order_by(TemplateMapping.tempID)
            result = session.scalars(stmt).all()
            return list(result)
