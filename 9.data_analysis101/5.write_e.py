파일을 읽는 방법을 봤으니 이번에는 파일을 쓰는 방법을 봅시다. 파일을 읽을 때와 마찬가지로 open 함수를 쓰면 됩니다. 첫번째 파라미터는 파일 이름을 넘겨주고, 두번째 파라미터는 'write'의 약자인 'w'를 넘겨주면 됩니다.

out_file = open('new_file.txt', 'w')
그리고 파일에 쓰려면 out_file에 write 메소드를 불러주면 됩니다. 엔터를 치기 위해서는 Newline Character("\n") 넣어주는 것도 잊지 마시고요.

out_file.write("Hello world!\n")
out_file.write("My name is Codeit!")
그리고 파일을 읽을 때와 마찬가지로 파일을 다 쓰면 꼭 닫아주는 것이 좋습니다.

out_file.close()
프로그램을 실행시키면 new_file.txt 파일이 생성되고, 파일에는 아래와 같은 내용이 있을 것입니다.

Hello world!
My name is Codeit!