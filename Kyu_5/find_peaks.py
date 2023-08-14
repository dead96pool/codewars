

def pickPeaks(arr):
    # return dict with position and values {pos: [1], peaks: [2]} 
   
    pos = []   # List to store positions of peaks
    peaks = [] # List to store values of peaks
    
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1]:
            if arr[i] > arr[i + 1]:
                pos.append(i)
                peaks.append(arr[i])
            elif arr[i] == arr[i + 1]:
                plateau_start = i
                
                # Traverse the plateau to find the beginning of the plateau-peak
                while i < len(arr) - 1 and arr[i] == arr[i + 1]:
                    i += 1
                    
                if i < len(arr) - 1 and arr[i] > arr[i + 1]:
                    pos.append(plateau_start)
                    peaks.append(arr[plateau_start])
    
    return {'pos': pos, 'peaks': peaks}

# Test cases
print(pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))

