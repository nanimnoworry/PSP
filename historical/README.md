# Historical Notebook Archive

이 디렉토리는 난임 프로젝트의 **공식 개발 과정에서 생성된 과거 노트북과 시각 자료**를 보존합니다.

## 원칙

- 과거 파일은 삭제하지 않습니다.
- 현재 실행/검증 계약에 직접 연결된 v6.2 계열은 저장소 루트에 유지합니다.
- historical 파일은 **기존 Git blob을 그대로 재사용해 이동**했으므로 내용 자체는 변경하지 않았습니다.
- 같은 이름의 팀 제공 최종 제출본과 GitHub historical notebook이 서로 다른 경우, 파일명보다 `deliverables/final_submission/MANIFEST.md`의 hash identity를 우선합니다.
- 실제 최종 발표의 모델 계보는 `docs/model_lineage.md`를 기준으로 해석합니다.

## 구조

```text
historical/
├── README.md
├── INDEX.md
├── notebooks/
│   ├── 00.Project_Fertility_PSP.ipynb
│   ├── 00.Project_Fertility_PSP_v3.ipynb
│   ├── 00.Project_Fertility_PSP_v4.ipynb
│   ├── 00.Project_Fertility_PSP_v5.ipynb
│   ├── 00.Project_Fertility_PSP_v5.1.ipynb
│   ├── 00.Project_Fertility_PSP_v6_experimental.ipynb
│   ├── 00_Project_Fertility_PSP_v6_3.ipynb
│   ├── prototype_PSP_Full_Code .ipynb
│   └── second_PSP_Full_Code.ipynb
└── assets/
    ├── second_PSP_Full_Code.png
    └── 스크린샷 2026-05-27 191231.png
```

이 파일들은 **공식 최종 제출물의 byte-identical archive라고 가정하지 않습니다.** 특히 historical의 `00.Project_Fertility_PSP_v5.ipynb`는 팀이 2026-08-08에 제공한 canonical final 제출본과 Git blob identity가 다릅니다.

## 현재 루트에 유지하는 실행 계열

```text
00.Project_Fertility_PSP_v6.2.ipynb
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
```

`scripts/validate_v6_2_notebook.py`가 final literature merged notebook의 루트 경로를 명시적으로 사용하므로, 재현성 계약을 깨뜨리지 않기 위해 해당 파일은 이동하지 않습니다.
