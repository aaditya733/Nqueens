/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package nqueens;

/**
 *
 * @author Aditya
 */

import java.util.*;

public class NQueens {
  int board[][];
  int N;
  int total;

  public NQueens(int n) {
    N = n;
    total = 0;
    board = new int[n][n];
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        board[i][j] = 0;
  }

  public boolean isSafe(int row, int col) {
    int i, j;
    for (i = 0; i < col; i++) {
      if (board[row][i] == 1)
        return false;
    }
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--) {
      if (board[i][j] == 1)
        return false;
    }
    for (i = row, j = col; j >= 0 && i < N; i++, j--) {
      if (board[i][j] == 1)
        return false;
    }
    return true;
  }

  public void solveNQUtil(int col) {    
    if (col >= N) {
      return;
    }
    for (int i = 0; i < N; i++) {
      if (isSafe(i, col)) {
        board[i][col] = 1;
        if (col == N-1) {
          total++;
        }
        solveNQUtil(col + 1);
        board[i][col] = 0;
      }
    }
  }

  public void solveNQ() {
    solveNQUtil(0);
    if (total == 0) {
      System.out.println("Solution does not exist for N = " + N);
      return;
    }
    System.out.println("Total solutions: " + total);
  }
  
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    NQueens NQ = new NQueens(N);
    NQ.solveNQ();
  }
}
