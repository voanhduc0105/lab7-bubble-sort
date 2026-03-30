# Bubble Sort Visualizer

A dual-mode bubble sort visualization tool that demonstrates the bubble sort algorithm step-by-step using either terminal-based text animation or an interactive PyGame graphical interface.

## Features

- **Terminal Mode**: Colored text-based visualization with real-time sorting steps
  - Blue highlights: elements being compared
  - Yellow highlights: elements being swapped
  - Green highlights: sorted portion of the array
  
- **PyGame Mode**: Interactive GUI visualization with performance metrics
  - Animated bar height representation
  - Real-time pass counters and comparison counts
  - Graphical legend for visual elements
  - Final summary screen with original vs. sorted arrays

## Requirements

- Python 3.7+
- `colorama` (for terminal mode)
- `pygame` (for PyGame mode)

Install dependencies:
```bash
pip install colorama pygame
```

## Usage

Run the program:
```bash
python main.py
```

Follow the prompts:
1. Confirm or modify `number_of_numbers` (defaults to 20)
2. Choose visualization mode:
   - **Mode 1**: Terminal animation with colored output
   - **Mode 2**: PyGame-based graphical interface

### Terminal Mode
- Clears screen between each step
- 0.25-second delay between comparisons
- Displays array index numbers and colored bar representations
- Shows pass count

### PyGame Mode
- Smooth frame-rate-controlled animation
- Displays comparison and pass counters
- Shows which elements have already been sorted (green bars)
- Press any key to exit after sorting completes

## Input Validation

- `number_of_numbers` must be a positive integer
- Minimum: 1 element
- Maximum: any reasonable value (tested with 20+)

## Algorithm

The visualizer implements the **bubble sort algorithm**:
1. Iterates through the array multiple passes
2. Each pass compares adjacent elements
3. Swaps elements if they are out of order
4. After each pass, the largest unsorted element settles to its final position
5. Continues until the array is fully sorted

**Time Complexity**: O(n²)  
**Space Complexity**: O(1)

## Implementation Notes

- The array is shuffled randomly at startup
- Both visualization modes operate on the same input data
- Original and sorted arrays are displayed for verification
- Generator-based step yielding allows smooth frame-by-frame animation

## Files

- `main.py` - Entry point with dual-mode visualizer and BubbleSort generator
- `JOURNAL.md` - Development log of interactions and changes
- `REPORT.md` - Project report and analysis

---

Built for educational demonstration of sorting algorithms and visualization techniques.
