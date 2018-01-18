import os, shutil

#classify I and C
# doclist_I = ["bb-cp-0001.txt",	"bb-cp-0004.txt",	"bb-cp-0005.txt",	"bb-cp-0007.txt",	"bb-cp-0012.txt",	"bb-cp-0014.txt",	"bb-cp-0026.txt",	"bb-cp-0030.txt",	"bb-cp-0038.txt",	"bb-cp-0040.txt",	"bb-cp-0044.txt",	"bb-cp-0048.txt",	"bb-cp-0074.txt",	"bb-cp-0075.txt",	"bb-cp-0104.txt",	"bb-cp-0105.txt",	"bb-cp-0108.txt",	"bb-cp-0109.txt",	"bb-cp-0121.txt",	"bb-cp-0123.txt",	"bb-cp-0125.txt",	"bb-cp-0127.txt",	"bb-cp-0128.txt",	"bb-cp-0129.txt",	"bb-cp-0130.txt",	"bb-cp-0132.txt",	"bb-cp-0134.txt",	"bb-cp-0136.txt",	"bb-cp-0138.txt",	"bb-cp-0140.txt",	"bb-cp-0142.txt",	"bb-cp-0144.txt",	"bb-cp-0146.txt",	"bb-cp-0156.txt",	"bb-cp-0158.txt",	"bb-cp-0162.txt",	"bb-cp-0164.txt",	"bb-cp-0166.txt",	"bb-cp-0168.txt",	"bb-cp-0171.txt",	"bb-cp-0172.txt",	"bb-cp-0174.txt",	"bb-cp-0176.txt",	"bb-cp-0178.txt",	"bb-cp-0180.txt",	"bb-cp-0182.txt",	"bb-cp-0184.txt",	"bb-cp-0186.txt",	"bb-cp-0188.txt",	"bb-cp-0190.txt",	"bb-cp-0192.txt",	"bb-cp-0194.txt",	"bb-cp-0196.txt",	"bb-cp-0198.txt",	"bb-cp-0200.txt",	"bb-cp-0202.txt",	"bb-cp-0204.txt",	"bb-cp-0206.txt",	"bb-cp-0208.txt",	"bb-cp-0210.txt",	"bb-cp-0212.txt",	"bb-cp-0214.txt",	"bb-cp-0218.txt",	"bb-cp-0220.txt",	"bb-cp-0222.txt",	"bb-cp-0223.txt",	"bb-cp-0225.txt",	"bb-cp-0227.txt",	"bb-cp-0229.txt",	"bb-cp-0231.txt",	"bb-cp-0233.txt",	"bb-cp-0235.txt",	"bb-cp-0237.txt",	"bb-cp-0239.txt",	"bb-cp-0241.txt",	"bb-cp-0242.txt",	"bb-cp-0244.txt",	"bb-cp-0246.txt",	"bb-cp-0248.txt",	"bb-cp-0250.txt",	"bb-cp-0252.txt",	"bb-cp-0254.txt",	"bb-cp-0256.txt",	"bb-cp-0257.txt",	"bb-cp-0259.txt",	"bb-cp-0261.txt",	"bb-cp-0263.txt",	"bb-cp-0265.txt",	"bb-cp-0267.txt",	"bb-cp-0269.txt",	"bb-cp-0271.txt",	"bb-cp-0273.txt",	"bb-cp-0275.txt",	"bb-cp-0277.txt",	"bb-cp-0279.txt",	"bb-cp-0281.txt",	"bb-cp-0283.txt",	"bb-cp-0285.txt",	"bb-cp-0287.txt",	"bb-cp-0289.txt",	"bb-cp-0291.txt",	"bb-cp-0293.txt",	"bb-cp-0295.txt",	"bb-cp-0297.txt",	"bb-cp-0299.txt",	"bb-cp-0301.txt",	"bb-cp-0303.txt",	"bb-cp-0305.txt",	"bb-cp-0307.txt",	"bb-cp-0309.txt",	"bb-cp-0312.txt",	"bb-cp-0314.txt",	"bb-cp-0316.txt",	"bb-cp-0318.txt",	"bb-cp-0320.txt",	"bb-cp-0322.txt",	"bb-cp-0324.txt",	"bb-cp-0338.txt",	"bb-cp-0340.txt",	"bb-cp-0342.txt",	"jpm-cp-0001.txt",	"sc-cp-0001.txt",	"sc-cp-0002.txt",	"sc-cp-0003.txt",	"sc-cp-0052.txt",	"sc-cp-0055.txt",	"sc-cp-0066.txt",	"sc-cp-0069.txt",	"sc-cp-0070.txt",	"sc-cp-0072.txt",	"sc-cp-0076.txt",	"sc-cp-0077.txt",	"sc-cp-0080.txt",	"sc-cp-0081.txt",	"sc-cp-0082.txt",	"sc-cp-0083.txt",	"sc-cp-0084.txt",	"sc-cp-0085.txt",	"sc-cp-0086.txt",	"sc-cp-0087.txt",	"sc-cp-0088.txt",	"sc-cp-0092.txt",	"sc-cp-0094.txt",	"sc-cp-0096.txt",	"sc-cp-0097.txt",	"sc-cp-0098.txt",	"sc-cp-0101.txt",	"sc-cp-0102.txt",	"sc-cp-0103.txt",	"sc-cp-0104.txt"
# ]
# doclist_C = ["bb-cp-0002.txt",	"bb-cp-0003.txt",	"bb-cp-0006.txt",	"bb-cp-0008.txt",	"bb-cp-0009.txt",	"bb-cp-0010.txt",	"bb-cp-0011.txt",	"bb-cp-0013.txt",	"bb-cp-0015.txt",	"bb-cp-0016.txt",	"bb-cp-0018.txt",	"bb-cp-0027.txt",	"bb-cp-0028.txt",	"bb-cp-0029.txt",	"bb-cp-0084.txt",	"bb-cp-0111.txt",	"bb-ic-0001.txt",	"bb-ic-0002.txt",	"bb-ic-0003.txt",	"bb-ic-0004.txt",	"bb-ic-0005.txt",	"bb-ic-0006.txt",	"bb-ic-0007.txt",	"bb-ic-0008.txt",	"bb-ic-0009.txt",	"bb-ic-0010.txt",	"bb-ic-0011.txt",	"bb-ic-0012.txt",	"bb-ic-0013.txt",	"bb-ic-0014.txt",	"bb-ic-0015.txt",	"bb-ic-0016.txt",	"bb-ic-0017.txt",	"bb-ic-0018.txt",	"bb-ic-0019.txt",	"bb-ic-0020.txt",	"bb-ic-0021.txt",	"bb-ic-0022.txt",	"bb-ic-0023.txt",	"bb-ic-0024.txt",	"bb-ic-0025.txt",	"bb-ic-0026.txt",	"bb-ic-0027.txt",	"bb-ic-0028.txt",	"bb-ic-0029.txt",	"bb-ic-0030.txt",	"bb-ic-0031.txt",	"bb-ic-0032.txt",	"bb-ic-0033.txt",	"bb-ic-0034.txt",	"rcg-ic-0001.txt",	"sc-cp-0004.txt",	"sc-cp-0005.txt",	"sc-cp-0006.txt",	"sc-cp-0007.txt",	"sc-cp-0008.txt",	"sc-cp-0009.txt",	"sc-cp-0010.txt",	"sc-cp-0011.txt",	"sc-cp-0012.txt",	"sc-cp-0013.txt",	"sc-cp-0014.txt",	"sc-cp-0015.txt",	"sc-cp-0016.txt",	"sc-cp-0017.txt",	"sc-cp-0018.txt",	"sc-cp-0019.txt",	"sc-cp-0020.txt",	"sc-cp-0021.txt",	"sc-cp-0022.txt",	"sc-cp-0023.txt",	"sc-cp-0024.txt",	"sc-cp-0025.txt",	"sc-cp-0026.txt",	"sc-cp-0027.txt",	"sc-cp-0028.txt",	"sc-cp-0029.txt",	"sc-cp-0030.txt",	"sc-cp-0031.txt",	"sc-cp-0032.txt",	"sc-cp-0033.txt",	"sc-cp-0034.txt",	"sc-cp-0035.txt",	"sc-cp-0037.txt",	"sc-cp-0038.txt",	"sc-cp-0039.txt",	"sc-cp-0040.txt",	"sc-cp-0041.txt",	"sc-cp-0042.txt",	"sc-cp-0043.txt",	"sc-cp-0044.txt",	"sc-cp-0045.txt",	"sc-cp-0047.txt",	"sc-cp-0048.txt",	"sc-cp-0049.txt",	"sc-cp-0050.txt",	"sc-cp-0053.txt",	"sc-cp-0054.txt",	"sc-cp-0056.txt",	"sc-cp-0057.txt",	"sc-cp-0058.txt",	"sc-cp-0059.txt",	"sc-cp-0060.txt",	"sc-cp-0061.txt",	"sc-cp-0062.txt",	"sc-cp-0063.txt",	"sc-cp-0064.txt",	"sc-cp-0065.txt",	"sc-ic-0001.txt",	"sc-ic-0002.txt",	"sc-ic-0003.txt",	"sc-ic-0004.txt",	"sc-ic-0005.txt",	"sc-ic-0006.txt",	"sc-ic-0007.txt",	"sc-ic-0008.txt",	"sc-ic-0009.txt",	"sc-ic-0010.txt"
# ]

#classify ratings in I
#doclist_neg2 = ["bb-cp-0001.txt",	"bb-cp-0048.txt",	"bb-cp-0204.txt",]
#doclist_neg1 = ["bb-cp-0004.txt",	"bb-cp-0005.txt",	"bb-cp-0012.txt",	"bb-cp-0014.txt",	"bb-cp-0074.txt",	"bb-cp-0075.txt",	"bb-cp-0121.txt",	"bb-cp-0123.txt",	"bb-cp-0125.txt",	"bb-cp-0128.txt",	"bb-cp-0136.txt",	"bb-cp-0138.txt",	"bb-cp-0140.txt",	"bb-cp-0146.txt",	"bb-cp-0171.txt",	"bb-cp-0182.txt",	"jpm-cp-0001.txt",	"sc-cp-0001.txt",	"sc-cp-0002.txt",	"sc-cp-0055.txt",	"sc-cp-0066.txt",	"sc-cp-0086.txt",
#]
#doclist_zero = ["bb-cp-0007.txt",	"bb-cp-0030.txt",	"bb-cp-0038.txt",	"bb-cp-0040.txt",	"bb-cp-0044.txt",	"bb-cp-0104.txt",	"bb-cp-0105.txt",	"bb-cp-0108.txt",	"bb-cp-0109.txt",	"bb-cp-0127.txt",	"bb-cp-0130.txt",	"bb-cp-0132.txt",	"bb-cp-0134.txt",	"bb-cp-0144.txt",	"bb-cp-0158.txt",	"bb-cp-0162.txt",	"bb-cp-0164.txt",	"bb-cp-0166.txt",	"bb-cp-0168.txt",	"bb-cp-0172.txt",	"bb-cp-0174.txt",	"bb-cp-0176.txt",	"bb-cp-0178.txt",	"bb-cp-0186.txt",	"bb-cp-0188.txt",	"bb-cp-0190.txt",	"bb-cp-0192.txt",	"bb-cp-0196.txt",	"bb-cp-0198.txt",	"bb-cp-0200.txt",	"bb-cp-0202.txt",	"bb-cp-0206.txt",	"bb-cp-0208.txt",	"bb-cp-0210.txt",	"bb-cp-0212.txt",	"bb-cp-0214.txt",	"bb-cp-0218.txt",	"bb-cp-0220.txt",	"bb-cp-0223.txt",	"bb-cp-0225.txt",	"bb-cp-0227.txt",	"bb-cp-0229.txt",	"bb-cp-0231.txt",	"bb-cp-0233.txt",	"bb-cp-0235.txt",	"bb-cp-0237.txt",	"bb-cp-0239.txt",	"bb-cp-0241.txt",	"bb-cp-0242.txt",	"bb-cp-0244.txt",	"bb-cp-0246.txt",	"bb-cp-0248.txt",	"bb-cp-0250.txt",	"bb-cp-0252.txt",	"bb-cp-0254.txt",	"bb-cp-0256.txt",	"bb-cp-0259.txt",	"bb-cp-0261.txt",	"bb-cp-0263.txt",	"bb-cp-0265.txt",	"bb-cp-0267.txt",	"bb-cp-0269.txt",	"bb-cp-0271.txt",	"bb-cp-0273.txt",	"bb-cp-0275.txt",	"bb-cp-0277.txt",	"bb-cp-0279.txt",	"bb-cp-0281.txt",	"bb-cp-0283.txt",	"bb-cp-0285.txt",	"bb-cp-0287.txt",	"bb-cp-0289.txt",	"bb-cp-0291.txt",	"bb-cp-0293.txt",	"bb-cp-0295.txt",	"bb-cp-0297.txt",	"bb-cp-0301.txt",	"bb-cp-0303.txt",	"bb-cp-0305.txt",	"bb-cp-0307.txt",	"bb-cp-0309.txt",	"bb-cp-0312.txt",	"bb-cp-0314.txt",	"bb-cp-0316.txt",	"bb-cp-0318.txt",	"bb-cp-0324.txt",	"bb-cp-0338.txt",	"bb-cp-0340.txt",	"bb-cp-0342.txt",	"sc-cp-0069.txt",	"sc-cp-0070.txt",	"sc-cp-0076.txt",	"sc-cp-0077.txt",	"sc-cp-0080.txt",	"sc-cp-0082.txt",	"sc-cp-0083.txt",	"sc-cp-0087.txt",	"sc-cp-0088.txt",	"sc-cp-0092.txt",	"sc-cp-0097.txt",	"sc-cp-0098.txt",	"sc-cp-0102.txt",	"sc-cp-0103.txt",	"sc-cp-0104.txt",
# ]
# doclist_pos1 = ["bb-cp-0026.txt",	"bb-cp-0129.txt",	"bb-cp-0142.txt",	"bb-cp-0156.txt",	"bb-cp-0180.txt",	"bb-cp-0184.txt",	"bb-cp-0194.txt",	"bb-cp-0222.txt",	"bb-cp-0257.txt",	"bb-cp-0299.txt",	"bb-cp-0320.txt",	"bb-cp-0322.txt",	"sc-cp-0003.txt",	"sc-cp-0052.txt",	"sc-cp-0072.txt",	"sc-cp-0081.txt",	"sc-cp-0084.txt",	"sc-cp-0085.txt",	"sc-cp-0094.txt",	"sc-cp-0096.txt",	"sc-cp-0101.txt",
# ]

#Classify ratings in C
doclist_neg1 = ["bb-ic-0012.txt",	"sc-cp-0009.txt",	"sc-cp-0053.txt",
]
doclist_zero = ["bb-cp-0002.txt",	"bb-cp-0011.txt",	"bb-cp-0013.txt",	"bb-cp-0015.txt",	"bb-cp-0016.txt",	"bb-cp-0018.txt",	"bb-cp-0027.txt",	"bb-cp-0028.txt",	"bb-cp-0029.txt",	"bb-cp-0111.txt",	"bb-ic-0001.txt",	"bb-ic-0002.txt",	"bb-ic-0004.txt",	"bb-ic-0005.txt",	"bb-ic-0006.txt",	"bb-ic-0007.txt",	"bb-ic-0009.txt",	"bb-ic-0013.txt",	"bb-ic-0014.txt",	"bb-ic-0015.txt",	"bb-ic-0016.txt",	"bb-ic-0017.txt",	"bb-ic-0018.txt",	"bb-ic-0019.txt",	"bb-ic-0023.txt",	"bb-ic-0024.txt",	"bb-ic-0025.txt",	"bb-ic-0026.txt",	"bb-ic-0028.txt",	"bb-ic-0030.txt",	"bb-ic-0031.txt",	"bb-ic-0032.txt",	"bb-ic-0033.txt",	"rcg-ic-0001.txt",	"sc-cp-0004.txt",	"sc-cp-0006.txt",	"sc-cp-0007.txt",	"sc-cp-0008.txt",	"sc-cp-0010.txt",	"sc-cp-0011.txt",	"sc-cp-0012.txt",	"sc-cp-0013.txt",	"sc-cp-0014.txt",	"sc-cp-0015.txt",	"sc-cp-0016.txt",	"sc-cp-0017.txt",	"sc-cp-0019.txt",	"sc-cp-0020.txt",	"sc-cp-0021.txt",	"sc-cp-0022.txt",	"sc-cp-0023.txt",	"sc-cp-0024.txt",	"sc-cp-0025.txt",	"sc-cp-0026.txt",	"sc-cp-0027.txt",	"sc-cp-0028.txt",	"sc-cp-0029.txt",	"sc-cp-0030.txt",	"sc-cp-0031.txt",	"sc-cp-0032.txt",	"sc-cp-0033.txt",	"sc-cp-0034.txt",	"sc-cp-0037.txt",	"sc-cp-0038.txt",	"sc-cp-0039.txt",	"sc-cp-0040.txt",	"sc-cp-0041.txt",	"sc-cp-0042.txt",	"sc-cp-0043.txt",	"sc-cp-0044.txt",	"sc-cp-0045.txt",	"sc-cp-0047.txt",	"sc-cp-0048.txt",	"sc-cp-0049.txt",	"sc-cp-0050.txt",	"sc-cp-0054.txt",	"sc-cp-0056.txt",	"sc-cp-0057.txt",	"sc-cp-0058.txt",	"sc-cp-0059.txt",	"sc-cp-0060.txt",	"sc-cp-0062.txt",	"sc-cp-0064.txt",	"sc-cp-0065.txt",	"sc-ic-0003.txt",	"sc-ic-0005.txt",	"sc-ic-0010.txt",
]
doclist_pos1 = ["bb-cp-0003.txt",	"bb-cp-0006.txt",	"bb-cp-0008.txt",	"bb-cp-0009.txt",	"bb-cp-0010.txt",	"bb-cp-0084.txt",	"bb-ic-0003.txt",	"bb-ic-0008.txt",	"bb-ic-0010.txt",	"bb-ic-0011.txt",	"bb-ic-0020.txt",	"bb-ic-0021.txt",	"bb-ic-0022.txt",	"bb-ic-0027.txt",	"bb-ic-0029.txt",	"bb-ic-0034.txt",	"sc-cp-0018.txt",	"sc-cp-0035.txt",	"sc-cp-0061.txt",	"sc-cp-0063.txt",	"sc-ic-0004.txt",	"sc-ic-0006.txt",	"sc-ic-0009.txt",
]
doclist_pos2 = ["sc-cp-0005.txt",	"sc-ic-0001.txt",	"sc-ic-0002.txt",	"sc-ic-0007.txt",	"sc-ic-0008.txt",	
]

#Copy the ducument in terms of ratings in I
# for filename in doclist_neg2:
	# # sourceDir1 = os.path.join("E:\NEWS", file)
	# # targetDir1 = os.path.join("E:\NEWS\I",file)
	# sourceDir1 = os.path.join(r"E:\NEWS", filename)
	# shutil.copy(sourceDir1,r"E:\NEWS\neg2")
	
# for filename in doclist_neg1:
	# sourceDir2 = os.path.join(r"E:\NEWS", filename)
	# shutil.copy(sourceDir2,r"E:\NEWS\neg1")
	
# for filename in doclist_zero:
	# sourceDir2 = os.path.join(r"E:\NEWS", filename)
	# shutil.copy(sourceDir2,r"E:\NEWS\zero")
	
# for filename in doclist_pos1:
	# sourceDir2 = os.path.join(r"E:\NEWS", filename)
	# shutil.copy(sourceDir2,r"E:\NEWS\pos1")
	

for filename in doclist_neg1:
	sourceDir2 = os.path.join(r"E:\NEWS", filename)
	shutil.copy(sourceDir2,r"E:\NEWS\neg1")
	
for filename in doclist_zero:
	sourceDir2 = os.path.join(r"E:\NEWS", filename)
	shutil.copy(sourceDir2,r"E:\NEWS\zero")
	
for filename in doclist_pos1:
	sourceDir2 = os.path.join(r"E:\NEWS", filename)
	shutil.copy(sourceDir2,r"E:\NEWS\pos1")

for filename in doclist_pos2:
	# sourceDir1 = os.path.join("E:\NEWS", file)
	# targetDir1 = os.path.join("E:\NEWS\I",file)
	sourceDir1 = os.path.join(r"E:\NEWS", filename)
	shutil.copy(sourceDir1,r"E:\NEWS\pos2")