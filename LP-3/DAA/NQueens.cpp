#include <iostream>
#include <vector>
using namespace std;

// Print the board
void printBoard(const vector<vector<int>> &board, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Check if placing a queen is safe
bool isSafe(const vector<vector<int>> &board, int row, int col, int N) {
    // Check column
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 1) return false;
    }

    // Check upper-left diagonal
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1) return false;
    }

    // Check upper-right diagonal
    for (int i = row - 1, j = col + 1; i >= 0 && j < N; i--, j++) {
        if (board[i][j] == 1) return false;
    }

    return true;
}

// Backtracking function
bool solveQueens(vector<vector<int>> &board, int row, int N) {
    if (row >= N) return true;

    for (int col = 0; col < N; col++) {
        if (board[row][col] == 1) {
            // Already placed (predefined queen)
            if (isSafe(board, row, col, N))
                return solveQueens(board, row + 1, N);
            else
                return false;
        }

        if (isSafe(board, row, col, N)) {
            board[row][col] = 1;
            if (solveQueens(board, row + 1, N)) return true;
            board[row][col] = 0;
        }
    }
    return false;
}

int main() {
    int N;
    cout << "Enter size of Board (N): ";
    cin >> N;

    vector<vector<int>> board(N, vector<int>(N, 0));

    int firstRow, firstCol;
    cout << "Enter position of first queen (row and col, 0-based): ";
    cin >> firstRow >> firstCol;

    board[firstRow][firstCol] = 1;

    if (solveQueens(board, 0, N)) {
        cout << "\nN-Queens Solution:\n";
        printBoard(board, N);
    } else {
        cout << "No possible solution exists.\n";
    }

    return 0;
}
