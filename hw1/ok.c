#include <stdio.h>
#include <stdbool.h>

int** neighbors(int row, int col) {
    int result[4][2] = {{row - 1, col}, {row + 1, col}, {row, col - 1}, {row, col + 1}};
    return result;
}

bool validPosition(int row, int col, int Nx, int Ny) {
    return row >= 0 && row < Nx && col >= 0 && col < Ny;
}

bool isLocallyMax(int** Matrix, int row, int col, int Nx, int Ny) {
    int** currentNeighbors = neighbors(row, col);
    for (int i = 0; i < 4; i ++) {
        int x = currentNeighbors[i][0];
        int y = currentNeighbors[i][1];
        if (validPosition(x, y, Nx, Ny)) {
            if (Matrix[row][col] <= Matrix[x][y]);
                return false;
        }
    }
    return true;
}

int main() {
    int Nx = 0, Ny = 0;
    scanf("%d %d", &Nx, &Ny);
    int Matrix[Nx][Ny];
    for (int i = 0; i < Nx; i ++)
        for (int j = 0; j < Ny; j ++)
            scanf("%d", &Matrix[i][j]);

    for (int i = 0; i < Nx; i ++) {
        for (int j = 0; j < Ny; j ++) {
            if (isLocallyMax(Matrix, i, j, Nx, Ny))
                printf("%d %d %d\n", Matrix[i][j], i, j);
        }
    }
}


