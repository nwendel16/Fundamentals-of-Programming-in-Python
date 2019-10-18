#Find the square area of Sacramento - 98 sq mi
#Convert area of Sacramento to sq ft - 2,732,083,200 sq ft
#Find area of city block - 168100 sq ft
#Find the number of blocks in the city - 16253 blocks

#Find the average number of trees per block
#Take 5 samples of city blocks, then average out the number of trees in a block
    #1. Land Park - 50
    #2. Midtown - 20
    #3. North Natomas - 35
    #4. Parkway - 20
    #5. North Sacramento - 25
#The average number of trees per block is 30

#Trees = Average * blocks
    #   30 * 16253 = 487590

#There are 487590 trees in Sacramento

miles = 98
feet = miles*(5280**2)
blkft = 168100
blocks = feet / blkft
avg = 30
trees = int(avg * blocks)
print('Would you like to know how many trees there are in Sacramento?' + ' yes or no')
yn = input()
if (yn == 'yes'):
    print('There are', trees, 'trees in Sacramento')
else:
    print('Too bad! There are', trees, 'trees in Sacramento')


