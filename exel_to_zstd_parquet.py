import pandas as pd

print("xlsx 읽는 중...")
df = pd.read_excel('2024년 국민여행조사_해외여행.xlsx')
print(f"완료! {df.shape[0]:,}행 x {df.shape[1]}열")

# 청크로 나눠서 저장
chunk_size = 10000
for i in range(0, len(df), chunk_size):
    chunk = df.iloc[i:i+chunk_size].astype(str)
    chunk.to_parquet(f'해외여행_part_{i//chunk_size}.zstd.parquet', compression='zstd')
    print(f"Part {i//chunk_size} 저장 완료")

