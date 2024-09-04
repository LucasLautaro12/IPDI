
import numpy as np
import imageio
import matplotlib.pyplot as plt

im = imageio.imread('imageio:chelsea.png')
print(im.shape,im.dtype)

# we are working in float numbers [0,1] in image processing:
im1 = np.clip(im /255.,0.,1.)
plt.imshow(im1[:,:,],'gray',vmin=0, vmax=1)
print(im1.shape,im1.dtype)
plt.show()

im5 = np.clip(im /255.,0.,1.) 
yiq=np.zeros(im5.shape)
yiq[:,:,0]=np.clip(0.229*im5[:,:,0]+0.587*im5[:,:,1]+0.114*im5[:,:,2],0,1)
yiq[:,:,1]=np.clip(0.59516*im5[:,:,0]-0.274453*im5[:,:,1]-0.321263*im5[:,:,2],-0.5957,0.5957)
yiq[:,:,2]=np.clip(0.211456*im5[:,:,0]-0.522591*im5[:,:,1]+0.311135*im5[:,:,2],-0.5226,0.5226)

plt.imshow(yiq[:,:,0],"gray")
plt.show()
plt.imshow(yiq[:,:,1],"gray")
plt.show()
plt.imshow(yiq[:,:,2],"gray")
plt.show()