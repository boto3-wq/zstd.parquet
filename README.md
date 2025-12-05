# Polars 설치 가이드

구형 CPU (AVX/AVX2 미지원) 환경에서는 기본 polars 대신 polars-lts-cpu를 설치해야 합니다.

## 설치
```bash
pip uninstall polars
pip install polars-lts-cpu
```

## 사용법

기존과 동일하게 사용하면 됩니다.
```python
import polars as pl
```
