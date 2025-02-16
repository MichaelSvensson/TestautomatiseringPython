'''
1 Vilka ekvivalensklasser har uttrycken?

1a. x > 100	
Giltiga värden: {101, 102, 103, ...} (alla heltal större än 100)
Ogiltiga värden: {... 98, 99, 100} (alla heltal mindre än eller lika med 100)

1b. y == 42	
Giltig klass: {42}
Ogiltig klass: {alla andra tal}

1c. len(text) >= 5   
Giltiga värden: {alla strängar med längd 5 eller större}
Ogiltiga värden: {alla strängar med längd mindre än 5}

1d. z == True	     
Giltig klass: {True}
Ogiltig klass: {False}

1e. 8 < v < 16     
Giltiga värden: {9, 10, 11, 12, 13, 14, 15}
Ogiltiga värden: {... 7, 8, 16, 17, ...}

1f. w == 32 or w == 64 or w == 128    
Giltiga värden: {32, 64, 128
Ogiltiga värden: {alla andra tal}

1g. if x < 5: … elif x < 10: … elif x < 15: … else   
Klass 1: {... -1, 0, 1, 2, 3, 4} (x < 5)
Klass 2: {5, 6, 7, 8, 9} (5 <= x < 10)
Klass 3: {10, 11, 12, 13, 14} (10 <= x < 15)
Klass 4: {15, 16, 17, ...} (x >= 15)

'''