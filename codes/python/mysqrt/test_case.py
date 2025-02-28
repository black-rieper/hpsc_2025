def test_1():
	from numpy import sqrt
	from mysqrt import sqrt2
	xvalues=[0,2,100,10000,0.001,1e8]
	small=1.0e-14
	for x in xvalues:
		s=sqrt2(x)
		s_numpy=sqrt(x)
		print(f"s={s} and s_numpy={s_numpy}")
		assert (s-s_numpy)<small, f"square root disagrees with numpy square root for x={x}"
		
	
