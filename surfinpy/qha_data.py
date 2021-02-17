from surfinpy import utils as ut

def qha_calc(qha_file, temp_r):
    """
    docstring
    """
    gibbs=[]
    gibbs = ut.read_vibdata(qha_file)
    gibbs = gibbs[1]

    return(gibbs)

