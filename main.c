#include <stdio.h>
#include "name.h"

void debug_name(NAME n) {
    printf("%s #%03d\n", NAME_names[n], n);
}

int main() {
    debug_name(state_ace);
    debug_name(state_act);
    debug_name(state_zap);
    debug_name(state_zip);
    return 0;
};