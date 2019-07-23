# VC = {klc: [expert, average, beginner] . . . . . . . . . . . . . . . . . . . . /* level of expertise */
# wrc: [low, medium, high] . . . . . . . . . . . . . . . . . . . . . . . /* willingness to take risks */
# idc: [shortterm, mediumterm, longterm] . . . . . . . . . . . /* duration of investment */
# awc: [yes, no] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /* advisory wanted ? */
# dsc: [savings, bonds, stockfunds, singleshares] . . . . . . /* direct product search */
# slc: [savings, bonds] . . . . . . . . . . . . . . . . . . . . . . . . /* type of low-risk investment */
# avc: [yes, no] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /* availability of funds */
# shc: [stockfunds, singlshares] . . . . . . . . . . . . . . /* type of high-risk investment */ }
# VPROD = {namep: [text] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /* name of the product */
# erp: [1..40] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /* expected return rate */
# rip: [low, medium, high] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /* risk level */
# mnivp: [1..14] . . . . . . . . . . . . /* minimum investment period of product in years */
# instp: [text] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /* financial institute */ }



# CR = {CR1: wrc = high!idc 6= shortterm,
# CR2: klc = beginner!wrc 6= high}
# CF = {CF1: idc = shortterm !mnivp < 3,
# CF2: idc = mediumterm !mnivp >=3 mnivp < 6,




# CF3: idc = longterm!mnivp  6,
# CF4: wrc = low!rip = low,
# CF5: wrc = medium!rip = low_rip = medium,
# CF6: wrc = high!rip = low_rip = medium_rip = high,
# CF7: klc = beginner!rip 6= high,
# CF8: slc = savings!namep = savings,
# CF9: slc = bonds!namep = bonds }
# CPROD = {CPROD1: namep =savings^erp =3^rip =low^mnivp =1^instp =A;
# CPROD2: namep = bonds^erp = 5^rip = medium^mnivp = 5^instp = B;
# CPROD3: namep = equity^erp = 9^rip = high^mnivp = 10^instp = B}
#





if __name__ == "__main__":
    n=2
    condition = "n=2"
#This shows that we can call a stored logical rule from neo4j and
    # #evaluate the str variable in python, can't say same for python ,need to verify that.
    if condition:
        print(condition)


    import random
    list = [20.5, 40.5, 30.5, 50.5, 70.5]
    random.seed(4)
    sample_list = random.sample(list, 3)
    print("random List", sample_list)

    sample_list = random.choices(list, k=1600)
    print("random List", sample_list)