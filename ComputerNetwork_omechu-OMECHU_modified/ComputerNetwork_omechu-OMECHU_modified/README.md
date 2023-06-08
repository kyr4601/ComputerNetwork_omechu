models.py 파일 삭제
==============
`init.py` 안에 함수로 `database.db` 파일 생성할 때      
미리 넣어둬야하는 음식들을 등록하도록 코드를 수정했습니다.

이 때, 기존에 `models.py`에서 정의했던 Dish 클래스를 사용하면 `init.py`에서 `models.py`를 import하고,         
`models.py`에서는 `init.py`를 import하는  __circular import__ 가 발생합니다.     
이 상태로 실행하면 임포트에러 때문에 실행이 안 돼서    
Dish 클래스를 `init.py` 내에서 정의했습니다.

 