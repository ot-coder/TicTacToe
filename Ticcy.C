#include <stdio.h>
#include <stdlib.h>
#include <time.h>




typedef struct{
    char board[9];
    char human;
    char ai;
}Ticcy;

void initialize_game(Ticcy *game){
    for (int i = 0; i < 9; i++){
        game ->board[i] = ' ';
    }
    game -> human = 'O';
    game ->ai = 'X';
    }

void print_board(Ticcy *game){
    for(int i = 0; i < 9; i++){
        printf("%c", game ->board[i]);
        if (i % 3 == 2){
            printf("\n");
            if (i != 8) printf("---------\n");
        }
        else{
            printf(" | ");
        }
    }
}

void available_moves(Ticcy *game){
    printf("Available moves: ");
    for (int i = 0; i < 9; i++){
        if(game -> board[i] == ' '){
             printf("%d", i);
        }
    }
    printf("\n");
}

int make_move(Ticcy *game, int position, char player){
    if(game -> board[position] == ' '){
        game ->board[position] =  player;
        return 1;
    }
    return 0;
}

int isBoard_Full( Ticcy *game){
    for(int i = 0; i < 9; i++){
        if(game -> board[i] == ' '){
            return 0;
        }
    }
    return 1;
}

char check_winner(Ticcy *game){

    for(int i = 0; i < 9; i +=3){
        if(game -> board[i] == game -> board[i + 1] &&
          game -> board[i] == game -> board[i + 2] && 
          game -> board[i] != ' '){
            return game -> board[i];
        }
    }

    for(int i = 0; i < 3; i++){
        if(game -> board[i] == game -> board[i + 3] &&
          game -> board[i] == game -> board[i + 6] && 
          game -> board[i] != ' '){
            return game -> board[i];
        }
    }

    if(game -> board[0] == game ->board[4]&&
       game ->board[0] == game ->board[8]){
        return game ->board[0];
    }

    if(game -> board[2] == game ->board[4]&&
       game ->board[0] == game ->board[6]){
        return game ->board[2];
    }

    return ' ';
    
}

int game_over(Ticcy *game){
    if(check_winner(game) != ' ' || isBoard_Full(game)){
        return 1;
    }
    return 0;
}

int minimax(Ticcy *game, int depth, int is_maximizing){
    char winner = check_winner(game);
    if(winner == 'X') return 1;
    if(winner == 'O') return -1;
    if(isBoard_Full(game)) return 0;

    if(is_maximizing) {
        int best_score = -9999;
        for(int i = 0; i < 9; i++){
            if(game ->board[i] == ' '){ 
                game ->board[i] = 'X';
                int score = minimax(game, depth + 1, 0);
                game ->board[i] = ' ';
                if(score > best_score){ best_score = score;}           
            }
        }
        return best_score;
    }else{
        int best_score = 9999;
        for(int i = 0; i < 9; i++){
            if(game ->board[i] == ' '){ 
                game ->board[i] = 'O';
                int score = minimax(game, depth + 1, 1);
                game ->board[i] = ' ';
                if(score < best_score){ best_score = score;}           
            }
        }
        return best_score;
    }
}

int main(){
    Ticcy game;
    initialize_game(&game);

    int ai_turn = rand() %2;

    while(!game_over(&game)){
        print_board(&game);
        if(ai_turn) {
            printf("\nThinking...\n");
            int best_score = -9999;
            int best_move = -1;
            for(int i = 0; i < 9; i++){
                if(game.board[i] == ' '){
                    game.board[i] = 'X';
                    int score = minimax(&game, 0,0);
                    game.board[i] = ' ';
                    if(score > best_score){
                        best_score = score;
                        best_move = i;
                    }
                }
            }
            make_move(&game, best_move, 'X');
        }else{
            printf("\nEnter in a position for your move(0-8): ");
            int move;
            scanf("%d", &move);
            if(!make_move(&game,move,'O')){
                printf("Invalid Move\n");
                continue;
            }
        }
        ai_turn = !ai_turn;
    }

    print_board(&game);
    char winner = check_winner(&game);
    if(winner == 'X'){ printf("\nPuny human, I WIN!!\n");}
    else if(winner == 'O'){printf("\nYou've prevailed... for now\n");}
    else{printf("\nIt a tie\n");}

    return 0;
}