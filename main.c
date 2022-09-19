#include <stdio.h>
#include "name.h"

void debug_name(NAME n) {
    printf("#%03d %s\n", n, NAME_names[n]);
}

int main() {
    debug_name(state_ape);
    debug_name(state_bag);
    debug_name(state_car);
    debug_name(state_fox);
    debug_name(state_zip);
    return 0;
};