import numpy as np

def ESlice(E1, E2, Eaxis):
	idx1=(np.abs(Eaxis-E1)).argmin()
	idx2=(np.abs(Eaxis-E2)).argmin()
	if(idx1<idx2):
		return slice(idx1,idx2)
	else:
		return slice(idx2,idx1)


