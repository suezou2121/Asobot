#! /usr/bin/env python
print("メッセージを入力すると適当な回答を行います。")
print("終了したいときは「さようなら」と入力してください")

quit=False
while not quit:
	message=raw_input(">")

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