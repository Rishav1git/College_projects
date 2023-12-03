#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct Point {
    int x, y;
};

struct Queue {
    struct Point* array;
    int front, rear, capacity;
};

struct Queue* createQueue(int capacity) {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->capacity = capacity;
    queue->front = 0;
    queue->rear = -1;
    queue->array = (struct Point*)malloc(queue->capacity * sizeof(struct Point));
    return queue;
}

bool isValid(int x, int y, int rows, int cols) {
    return (x >= 0 && x < rows && y >= 0 && y < cols);
}

bool isSafe(char** maze, int x, int y, int rows, int cols) {
    return (isValid(x, y, rows, cols) && maze[x][y] != '#');
}

void enqueue(struct Queue* queue, int x, int y) {
    queue->rear++;
    queue->array[queue->rear].x = x;
    queue->array[queue->rear].y = y;
}

struct Point dequeue(struct Queue* queue) {
    struct Point item = queue->array[queue->front];
    queue->front++;
    return item;
}

void displayMaze(char** maze, int rows, int cols, struct Point start, struct Point end) {
    printf("Maze:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (i == start.x && j == start.y) {
                printf("S ");
            } else if (i == end.x && j == end.y) {
                printf("E");
            } else {
                printf("%c ", maze[i][j]);
            }
        }
        printf("\n");
    }
}


bool solveMaze(char** maze, int rows, int cols, struct Point start, struct Point end) {
    int** visited = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        visited[i] = (int*)calloc(cols, sizeof(int));
    }

    int dx[] = { -1, 0, 1, 0 };
    int dy[] = { 0, 1, 0, -1 };

    struct Queue* queue = createQueue(rows * cols);
    visited[start.x][start.y] = 1;
    enqueue(queue, start.x, start.y);

    while (queue->front <= queue->rear) {
        struct Point current = dequeue(queue);

        if (current.x == end.x && current.y == end.y) {
            printf("Path found!\n");
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    if (visited[i][j] == 1) {
                    maze[i][j] = '+';
                }
                    
                }
                // printf("\n");
            }
            displayMaze(maze, rows, cols, start, end); 
            return true;
        }

        for (int i = 0; i < 4; i++) {
            int newX = current.x + dx[i];
            int newY = current.y + dy[i];

            if (isSafe(maze, newX, newY, rows, cols) && !visited[newX][newY]) {
                visited[newX][newY] = 1;
                enqueue(queue, newX, newY);
            }
        }
    }
    printf("No path found!\n");
    for (int i = 0; i < rows; i++) {
        free(visited[i]);
    }
    free(visited);
    return false;
}

int main() {
    //user input
    int rows, cols;
    puts("Enter the number of rows");
    scanf("%d", &rows);
    puts("Enter the number of columns");
    scanf("%d", &cols);

    // Clear newline from the input buffer
    while (getchar() != '\n');

    printf("Enter the maze (%dx%d):\n", rows, cols);
    char** maze = (char**)malloc(rows * sizeof(char*));
    for (int i = 0; i < rows; i++) {
        maze[i] = (char*)malloc((cols + 1) * sizeof(char)); // +1 for null terminator
        scanf("%s", maze[i]);
    }

    struct Point start = { 0, 0 };
    struct Point end = { rows - 1, cols - 1 };

    displayMaze(maze, rows, cols, start, end); 
    solveMaze(maze, rows, cols, start, end);

    // Free dynamically allocated memory
    for (int i = 0; i < rows; i++) {
        free(maze[i]);
    }
    free(maze);

    return 0;
}
