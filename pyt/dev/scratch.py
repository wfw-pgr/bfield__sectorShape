import numpy as np
import nkBasicAlgs.integrate__GaussLegendre as igl


# ========================================================= #
# ===  test calculation                                 === #
# ========================================================= #

def scratch():

    x_, y_, z_ = 0, 1, 2
    bx_,by_,bz_= 3, 4, 5

    # ------------------------------------------------- #
    # --- [1] make coordinate                       --- #
    # ------------------------------------------------- #
    import nkUtilities.equiSpaceGrid as esg
    x1MinMaxNum = [              0.4,              1.2, 101 ]
    x2MinMaxNum = [  0.0/180.0*np.pi, 90.0/180.0*np.pi, 101 ]
    x3MinMaxNum = [              0.1,              0.1,   1 ]
    coord       = esg.equiSpaceGrid( x1MinMaxNum=x1MinMaxNum, x2MinMaxNum=x2MinMaxNum, \
                                     x3MinMaxNum=x3MinMaxNum, returnType = "point" )

    # ------------------------------------------------- #
    # --- [2] functions                             --- #
    # ------------------------------------------------- #
    def zpos_coil( radii, theta ):
        zpos   = np.zeros( (radii.shape[0],) )
        zpos   = zpos + 0.1
        return( zpos )
        
    def Kleeven2016( rp, th, r0=0.0, th0=0.0, zp=1.0, alpha=0.0, J0=1.0 ):
        insqrt = np.sqrt( ( rp - r0*np.cos( th - th0 ) )**2 + r0**2*( np.sin( th-th0 ) )**2 + zp**2 )
        ret    = J0 / ( 4.0 * np.pi ) * zp * rp * np.cos( alpha ) / insqrt**3
        return( ret )

    # ------------------------------------------------- #
    # --- [3] parameters of function                --- #
    # ------------------------------------------------- #
    r0    = coord[:,0]
    th0   = coord[:,1]
    zp    = coord[:,2]
    J0    = 1.0
    alpha = 0.0

    # ------------------------------------------------- #
    # --- [4] integration                           --- #
    # ------------------------------------------------- #
    x1Range = [ 0.7, 0.8 ]
    x2Range = [ 30.0/180.0*np.pi, 50.0/180.0*np.pi ]
    nPoints = coord.shape[0]
    bz      = np.zeros( (nPoints,) )
    for ik in list( range( nPoints ) ):
        kwargs  = { "r0":coord[ik,0], "th0":coord[ik,1], "zp":coord[ik,2], \
                    "J0":J0, "alpha":alpha }
        bz[ik]  = igl.integrate__GaussLegendre( function=Kleeven2016, kwargs=kwargs, \
                                                x1Range=x1Range, x2Range=x2Range )
    bfield        = np.zeros( (nPoints,6,) )
    bfield[:, x_] = coord[:,0] * np.cos( coord[:,1] )
    bfield[:, y_] = coord[:,0] * np.sin( coord[:,1] )
    bfield[:, z_] = coord[:,2]
    bfield[:,bz_] = bz

    # ------------------------------------------------- #
    # --- [5] save in a file                        --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    outFile   = "dat/bfield.dat"
    spf.save__pointFile( outFile=outFile, Data=bfield )

    # ------------------------------------------------- #
    # --- [6] draw colormap                         --- #
    # ------------------------------------------------- #
    import nkUtilities.load__config   as lcf
    import nkUtilities.cMapTri        as cmt
    config                   = lcf.load__config()
    pngFile                  = "png/bfield.png"
    config["FigSize"]        = [6,6]
    config["cmp_position"]   = [0.16,0.16,0.90,0.86]
    config["xTitle"]         = "X (m)"
    config["yTitle"]         = "Y (m)"
    config["cmp_xAutoRange"] = True
    config["cmp_yAutoRange"] = True
    config["cmp_xRange"]     = [-1.0,+1.0]
    config["cmp_yRange"]     = [-1.0,+1.0]

    cmt.cMapTri( xAxis=bfield[:,x_], yAxis=bfield[:,y_], cMap=bfield[:,bz_], \
    	         pngFile=pngFile, config=config )


    
    
# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):

    scratch()


