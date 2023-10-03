int a = 8;
const int b = 5;

int main() {
    int *p = &a;
    *p = 10;
    p = &b;
    *p = 20;
    return 0;
}
