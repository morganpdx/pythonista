#!/usr/bin/python3


def translate_me(raw_string):
	alpha_list = string.ascii_lowercase
	puncts = string.punctuation

	string.maketrans()

	print alpha_list
	print puncts

translate_me("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")



# >>> frm = 'acdefhnoprstuw'
# >>> to = 'אקדיפהנופרסתאו'
# >>> trans_table = str.maketrans(frm, to)
# >>> hebrew_phrase = 'fear cuts deeper than swords'.translate(trans_table)
# >>> hebrew_phrase