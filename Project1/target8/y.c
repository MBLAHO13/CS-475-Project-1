#include <stdio.h>
#include <dlfcn.h>

main() {
        void *h, *p;

        h = dlopen(NULL, RTLD_LAZY);
        p = dlsym(h, "system");
        printf("0x%08x\n", p);
        p = dlsym(h, "exit");
        printf("0x%08x\n", p);
}
