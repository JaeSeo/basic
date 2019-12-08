strip 메소드는 문자열의 가장 앞쪽과 뒤쪽에 있는 화이트 스페이스(white space)가 제거된 새로운 문자열을 리턴해줍니다.

print("    Hello world!     ".strip())
Hello world!
화이트 스페이스는 그냥 띄어쓰기(" ") 뿐만 아니라 탭("\t")과 엔터("\n")까지 포괄적으로 얘기하는 것입니다.

print(" \n\t   Hello world!   \n\n\t\n  ".strip())
Hello world!
하지만 strip은 문자열의 가장 앞쪽과 뒤쪽에 있는 화이트 스페이스만 제거하지, 중간 중간 있는 화이트 스페이스는 그대로 둔다는 것을 기억합시다.

print(" \n\t   Hello      wo\nrld!   \n\n\t\n  ".strip())
Hello      wo
rld!