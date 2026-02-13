# Requiremnt for refactoring

## DataBase

### table name change

- api_definition => api_mst
- parameter_definition ==> api_param
- user_input ==> job_mst

## column name change

- api_mst 테이블에 request_type 칼럼 추가 ( POST, GET 방식 관리)
- program_name ==> api_name

## pk 관련

- api_mst 의 pk 는 api_name 으로 변경하고 id 는 삭제
- api_param 의 pk, fk 는 api_name 으로 처리
- job_mst 의 api_name 의 fk 로 처리

## sql Model class name change

- APIDefinition ==> APIMst
- ParameterDefinition ==> APIParam
- UserInput ==> JobMst
- column_name, pk, fk 변경사항 반영

## 결과 적재 테이블

- id 가 auto increment 형식이라 api call 마다 중복된 데이터가 적재되고 있음.
- 중복 데이터를 사전에 체크하는 방안
- 결과를 단순히 적재하는 테이블과 분석용으로 정제된 데이터를 관리하는 테이블로 분리하는 방안

## loggging 분리

[ok] logs 폴더에 logging 관련 소스 분리
[ok] 모든 py 파일은 logs 폴더의 소스 참조
