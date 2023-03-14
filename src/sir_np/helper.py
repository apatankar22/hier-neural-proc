def help_run(x1, x2, ep):
		return ("At epoch " + str(ep) + " loss " + str(((x1**2 + x2**2) - ((x1-1)**2 + (x2-1)**2))/1000))