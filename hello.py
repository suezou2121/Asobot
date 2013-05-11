#! /usr/bin/env python
import re
print("メッセージを入力すると適当な回答を行います。")
print("終了したいときは「さようなら」と入力してください")

pattern = re.compile(r'「(.+?)」は「(.+?)」')
pattern2 = re.compile(r'「(.+?)」は[\?？]')

dic={}

quit=False
while not quit:
	message=raw_input(">")
	res=False

	iterator = pattern.finditer(message)
	for match in iterator:
	    dic[match.group(1)]=match.group(2) 
	    res=True
	    print(match.group(0)+"ですね。覚えました。")

	iterator = pattern2.finditer(message)
	for match in iterator:
		res=True
		if match.group(1) in dic:
			print(dic[match.group(1)]+"です。")
		else:
			print("知りませんそんなこと")

	if message=="おはよう" and not res:
		res=True
		print("おはようございます")
	elif message=="こんにちは":
		res=True
		print("おはようございます")
	elif message=="こんばんは":
		res=True
		print("おやすみなさい")
	elif message=="さようなら":
		res=True
		quit=True

	if not res:
		print("え?　なんだって?")

print("さようなら～")