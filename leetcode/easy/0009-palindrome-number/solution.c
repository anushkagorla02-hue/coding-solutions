bool isPalindrome(int x) {
    int rem,temp;
    long long rev=0;
    temp=x;
    while(x>0){
         rem=x %10;
         rev = rev*10+rem;
         x=x/10;
    }
    if(temp==rev)
      return true;
    else
      return false;
}