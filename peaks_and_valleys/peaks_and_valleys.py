def find_peaks(data):
    peaks = []

    for i, datum in enumerate(data):
        if 0 < i < len(data)-1:
            if data[i-1] < datum > data[i+1]:
                peaks.append(i)

    return peaks
    
def find_valleys(data):
    valleys = []

    for i, datum in enumerate(data):
        if 0 < i < len(data)-1:
            if data[i-1] > datum < data[i+1]:
                valleys.append(i)

    return valleys

def find_peaks_and_valleys(peaks, valleys):
    peaks_and_valleys = peaks + valleys

    return peaks_and_valleys

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    
    peaks = find_peaks(data)
    valleys = find_valleys(data)
    peaks_and_valleys = find_peaks_and_valleys(peaks, valleys)

    print(f"Peaks: {peaks}")
    print(f"Valleys: {valleys}")
    print(f"Peaks and Valleys: {peaks_and_valleys}")
main()