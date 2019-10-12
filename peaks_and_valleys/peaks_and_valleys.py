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

def largest_peak(data):
    largest = 0
    for datum in data:
        if datum > largest:
            largest = datum
    
    return largest

def display(data):
    graph = []
    top = largest_peak(data)
    
    for i, datum in enumerate(data):
        row = []
        while len(row) < top:
            if len(row) < datum:
                row.append("X")
            else:
                row.append(" ")
            
        graph.append(row)
    
    graph = list(map(list, zip(*graph)))[::-1]

    for row in graph:
        graph_row = ""
        for col in row:
            graph_row += f"{col} "
        print(graph_row)
    return graph

def pour_water(data, peaks):
    print(f"{data}")
    between_peaks = []
    for i, datum in enumerate(data):
        if datum in peaks:
            between_peaks.append(i)

    print(f"between_peaks: {between_peaks}")

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    
    peaks = find_peaks(data)
    valleys = find_valleys(data)
    peaks_and_valleys = find_peaks_and_valleys(peaks, valleys)

    display(data)
    pour_water(data, peaks)

    print(f"Peaks: {peaks}")
    print(f"Valleys: {valleys}")
    print(f"Peaks and Valleys: {peaks_and_valleys}")
main()