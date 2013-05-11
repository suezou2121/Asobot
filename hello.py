#! /usr/bin/env python
import re
print("メッセージを入力すると適当な回答を行います。")
print("終了したいときは「さようなら」と入力してください")

# text = "「あなたの名前」は「asobot」"
pattern = re.compile(r'「(.+?)」は「(.+?)」')
pattern2 = re.compile(r'「(.+?)」は\?')


dic={}


quit=False
while not quit:
	message=raw_input(">")

	iterator = pattern.finditer(message)
	for match in iterator:
	    dic[match.group(1)]=match.group(2) 
	    print(match.group(0)+"ですね。覚えました。")

	iterator = pattern2.finditer(message)
	for match in iterator:
		if match.group(1) in dic:
			
			print(dic[match.group(1)]+"です。")

		else:
			print("知りませんそんなこと")
	if message=="おはよう":
		print("おはようございます")
		pass
	elif message=="こんにちは":
		print("おはようございます")
		pass
	elif message=="こんばんは":
		print("おやすみなさい")
		pass
	elif message=="さようなら":
		quit=True
		pass
	pass

print("さようなら～")