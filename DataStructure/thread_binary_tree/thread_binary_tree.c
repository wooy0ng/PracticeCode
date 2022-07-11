#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node* nodePointer;

typedef struct node{
    short int left_thread;
    nodePointer left_child;
    int data;
    nodePointer right_child;
    short int right_thread;
}node;

struct node *insucc(nodePointer ptr){
    if (ptr->right_thread == true)
        return ptr->right_child;
    ptr = ptr->right_child;
    while (ptr->left_thread == false){
        ptr = ptr->left_child;
    }
    return ptr;
};

void inorder(nodePointer root){
    if (root == NULL)
        printf("empty tree");
    
    nodePointer ptr = root;
    while (ptr->left_thread == false)
        ptr = ptr->left_child;  

    while (ptr != NULL){
        printf("%3d", ptr->data);
        ptr = insucc(ptr);
    }
}

struct node *insert(nodePointer root, char data){
    nodePointer ptr = root;
    nodePointer parent = NULL;
    
    while (ptr != NULL){
        if (data == (ptr->data)){
            return root;
        }
        parent = ptr;
        if (data < ptr->data){
            if (ptr->left_thread == false)
                ptr = ptr->left_child;
            else
                break;
        }
        else{
            if (ptr->right_thread == false)
                ptr = ptr->right_child;
            else
                break;
        }
    }

    // create new node
    nodePointer tmp = (nodePointer)malloc(sizeof(node));
    tmp->data = data;
    tmp->left_thread = true;
    tmp->right_thread = true;

    if (parent == NULL){
        root = tmp;
        tmp->left_child = NULL;
        tmp->right_child = NULL;
    }
    else if (data < (parent->data)){
        tmp->left_child = parent->left_child;
        tmp->right_child = parent;
        parent->left_thread = false;
        parent->left_child = tmp;
    }
    else{
        tmp->left_child = parent;
        tmp->right_child = parent->right_child;
        parent->right_thread = false;
        parent->right_child = tmp;
    }
    return root;
}

void delete(nodePointer root, int data){
    nodePointer dest = root->left_child;
    nodePointer ptr = root;

    if (root->data != data){
        while (true){
            if (dest->data < data){
                if (dest->right_thread)
                    return;
                ptr = dest;
                dest = dest->right_child;
            }
            else if (dest->data > data){
                if (dest->left_thread)
                    return;
                ptr = dest;
                dest = dest->left_child;
            }
            else{
                // catch data
                break;
            }
        }
    }
    else{
        dest = root;
    }

    nodePointer target = dest;
    if (!dest->right_thread && !dest->left_thread){
        ptr = dest;
        target = dest->left_child;
        while (!target->right_thread){
            ptr = target;
            target = target->right_child;
        }
        dest->data = target->data;
    }
    
    if (ptr->data >= target->data){
        if (target->right_thread && target->left_thread){
            ptr->left_child = target->left_child;
            ptr->left_thread = true;
        }
        else if (target->right_thread){
            // max
            nodePointer largest = target->left_child;
            while (!largest->right_thread){
                largest = largest->right_child;
            }
            largest->right_child = ptr;
            ptr->left_child = target->left_child;
        }
        else{
            // min
            nodePointer smallest = target->right_child;
            while (!smallest->left_thread){
                smallest = smallest->left_child;
            }
            smallest->left_child = target->left_child;
            ptr->left_child = target->right_child;
        }
    }
    else{
        if (target->right_thread && target->left_thread){
            ptr->right_child = target->right_child;
            ptr->right_thread = true;
        }
        else if (target->right_thread){
            // max
            nodePointer largest = target->left_child;
            while (!largest->right_thread){
                largest = largest->right_child;
            }
            largest->right_child = ptr;
            ptr->left_child = target->left_child;
        }
        else{
            // min
            nodePointer smallest = target->right_child;
            while (!smallest->left_thread){
                smallest = smallest->left_child;
            }
            smallest->left_child = target->left_child;
            ptr->left_child = target->right_child;            
        }
    }
}


int main(){
    nodePointer root = NULL;

    root = insert(root, 30);
    root = insert(root, 20);
    root = insert(root, 50);
    root = insert(root, 5);
    root = insert(root, 13);

    // check
    inorder(root);
    printf("\n");

    delete(root, 30);
    inorder(root);
    printf("\n");

    return 0; 
}