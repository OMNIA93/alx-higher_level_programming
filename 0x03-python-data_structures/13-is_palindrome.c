#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t   *h = *head;
    int         T[2000], len = 0, i = 0;

    while (h)
    {
        T[len] = h->n;
        len++;
        h = h->next;
    }
    len--;
    while (i < len)
    {
        if (T[len] != T[i])
            return (0);
        i++;
        len--;
    }
    return (1);
}
