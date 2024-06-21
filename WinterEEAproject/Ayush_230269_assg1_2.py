import cv2
import numpy as np
import matplotlib.pyplot as plt


s1 = r"C:\Users\Ayush's Galaxy Book\Pictures\Screenshots\Screenshot 2024-02-06 104614.png"
s2 = r"C:\Users\Ayush's Galaxy Book\Pictures\Screenshots\Screenshot 2024-02-06 104632.png" 
def hybrid(s1,s2):
    img1 = cv2.imread(s1,cv2.IMREAD_GRAYSCALE)
    # assert img1 is not None, "file could not be read, check with os.path.exists()"
    reimg1 = cv2.resize(img1,(256,256))
    img2 = cv2.imread(s2,cv2.IMREAD_GRAYSCALE)
    # assert img2 is not None, "file could not be read, check with os.path.exists()"
    reimg2 = cv2.resize(img2,(256,256))
    assert reimg1 is not None, "file could not be read, check with os.path.exists()"
    dft1 = cv2.dft(np.float32(reimg1),flags= cv2.DFT_COMPLEX_OUTPUT)
    dft_shift1 = np.fft.fftshift(dft1)

    magnitude_spectrum1 = 20*np.log(cv2.magnitude(dft_shift1[:,:,0],dft_shift1[:,:,1]))
    dft1 = np.fft.fft2(reimg1, axes=(0,1))
    dft_shift1 = np.fft.fftshift(dft1)
    assert reimg2 is not None, "file could not be read, check with os.path.exists()"
    dft2 = cv2.dft(np.float32(reimg2),flags= cv2.DFT_COMPLEX_OUTPUT)
    dft_shift2 = np.fft.fftshift(dft2)

    magnitude_spectrum2 = 20*np.log(cv2.magnitude(dft_shift2[:,:,0],dft_shift2[:,:,1]))
    dft2 = np.fft.fft2(reimg2, axes=(0,1))
    dft_shift2 = np.fft.fftshift(dft2)
    #mask1
    mask1 = np.zeros_like(reimg1)
    cy = mask1.shape[0] // 2
    cx = mask1.shape[1] // 2
    cv2.rectangle(mask1,(cx-16,cy+16),(cx+16,cy-16),(255,255,255),-1)[0]
    #
    dft_shift_masked1 = np.multiply(dft_shift1,mask1) / 255
    
    back_ishift1 = np.fft.ifftshift(dft_shift1)
    back_ishift_masked1 = np.fft.ifftshift(dft_shift_masked1)
    # magnitude_spectrum11 = 20*np.log(cv2.magnitude(back_ishift_masked1[:,:,0],back_ishift_masked1[:,:,1]))

    img_back1 = np.fft.ifft2(back_ishift1, axes=(0,1))
    img_filtered1 = np.fft.ifft2(back_ishift_masked1, axes=(0,1))

    img_back1 = np.abs(img_back1).clip(0,255).astype(np.uint8)
    img_filtered1 = np.abs(img_filtered1).clip(0,255).astype(np.uint8)

    dft11 = cv2.dft(np.float32(img_filtered1),flags= cv2.DFT_COMPLEX_OUTPUT)
    dft_shift11 = np.fft.fftshift(dft11)

    magnitude_spectrum11 = 20*np.log(cv2.magnitude(dft_shift11[:,:,0],dft_shift11[:,:,1]))

    mask2 = np.zeros_like(reimg2)
    cy = mask2.shape[0] // 2
    cx = mask2.shape[1] // 2
    cv2.rectangle(mask2,(cx-16,cy+16),(cx+16,cy-16),(255,255,255),-1)[0]
    mask2 = 255 - mask2

    dft_shift_masked2 = np.multiply(dft_shift2,mask2) / 255

    back_ishift = np.fft.ifftshift(dft_shift2)
    back_ishift_masked2 = np.fft.ifftshift(dft_shift_masked2)
    # magnitude_spectrum22 = 20*np.log(cv2.magnitude(back_ishift_masked2[:,:,0],back_ishift_masked2[:,:,1]))

    img_back2 = np.fft.ifft2(back_ishift, axes=(0,1))
    img_filtered2 = np.fft.ifft2(back_ishift_masked2, axes=(0,1))

    img_back2 = np.abs(img_back2).clip(0,255).astype(np.uint8)
    img_filtered2 = np.abs(3*img_filtered2).clip(0,255).astype(np.uint8)

    dft22 = cv2.dft(np.float32(img_filtered2),flags= cv2.DFT_COMPLEX_OUTPUT)
    dft_shift22 = np.fft.fftshift(dft22)

    magnitude_spectrum22 = 20*np.log(cv2.magnitude(dft_shift22[:,:,0],dft_shift22[:,:,1]))


    
    
    img_c = img_filtered1 + img_filtered2

    plt.subplot(191),plt.imshow(magnitude_spectrum1, cmap= 'gray')
    plt.title('FFT Img1'),plt.xticks([]),plt.yticks([])
    plt.subplot(192),plt.imshow(magnitude_spectrum2, cmap= 'gray')
    plt.title('FFT Img2'),plt.xticks([]),plt.yticks([])
    plt.subplot(193),plt.imshow(img_filtered1,cmap='gray')
    plt.title('HPF Img1'),plt.xticks([]),plt.yticks([])
    plt.subplot(194),plt.imshow(img_filtered2, cmap= 'gray')
    plt.title('LPF Img2'),plt.xticks([]),plt.yticks([])
    plt.subplot(195),plt.imshow(mask1,cmap= 'gray')
    plt.title('Mask1'),plt.xticks([]),plt.yticks([])
    plt.subplot(196),plt.imshow(mask2, cmap= 'gray')
    plt.title('Mask2'),plt.xticks([]),plt.yticks([])
    plt.subplot(197),plt.imshow(magnitude_spectrum11, cmap='gray')
    plt.title('FFT of HPF'),plt.xticks([]),plt.yticks([])
    plt.subplot(198),plt.imshow(magnitude_spectrum22, cmap='gray')
    plt.title('FFT of LPF'),plt.xticks([]),plt.yticks([])
    plt.subplot(199),plt.imshow(img_c, cmap='gray')
    plt.title('Hybrid'),plt.xticks([]),plt.yticks([])
    plt.subplot(321),plt.imshow(reimg1,cmap='gray')
    plt.title('Img1'),plt.xticks([]),plt.yticks([])
    plt.subplot(322),plt.imshow(reimg2,cmap='gray')
    plt.title('Img2'),plt.xticks([]),plt.yticks([])
    plt.show()
    # cv2.imshow("Mask",mask1)
    # cv2.waitKey(0)

hybrid(s1,s2)