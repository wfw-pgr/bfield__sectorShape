

def unpack_kw( arg1, arg2, kw1="kw1", kw2="kw2" ):
    print( "Hello, I am {0}, program to say {1}.".format(kw1,kw2) )
    print( arg1 )
    print( arg2 )
    return()


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    kw1 = "link"
    kw2 = "tri-force"
    unpack_kw( "blabla1", "blabla2", kw1=kw1, kw2=kw2 )

    dictionary = { "arg2":"blabla1","arg1":"blabla2","kw1":kw1, "kw2":kw2 }
    dictionary = { "kw1":kw1, "kw2":kw2 }
    dictionary = { "kw2":"zelda" }
    unpack_kw( "heyhey1", "heyhey2", **dictionary )
