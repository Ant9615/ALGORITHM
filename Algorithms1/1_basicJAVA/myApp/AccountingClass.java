package myApp;

class AccountingApp{ // 먼저 선언된 클래스 명 사용 불가
    public double valueOfSupply;
    public double VATRate;
    public double expenseRate;

    public double getVAT(){
        return valueOfSupply * VATRate;
    } // 메소드

    public double getTotal(){
        return valueOfSupply + getVAT();
    }

    public double getExpense(){
        return valueOfSupply * expenseRate;
    }

    public double getIncome(){
        return valueOfSupply - getExpense();
    }

    public double getDividend_1(){
        return getIncome() * 0.5;
    }

    public double getDividend_2(){
        return getIncome() * 0.3;
    }

    public double getDividend_3(){
        return getIncome() * 0.2;
    }

    public void print(){
        System.out.println("===============================");
        System.out.println("Value of Supply: "+ valueOfSupply);
        System.out.println("VAT: "+getVAT());
        System.out.println("Total: "+getTotal());
        System.out.println("Expense: "+getExpense());
        System.out.println("Income: "+getIncome());
        System.out.println("Dividend_1: "+getDividend_1());
        System.out.println("Dividend_2: "+getDividend_2());
        System.out.println("Dividend_3: "+getDividend_3());
        System.out.println("===============================");
    }
}

public class AccountingClass {
    public static void main(String[] args) {
        // AccountingApp.valueOfSupply = 10000.0;
        // AccountingApp.VATRate = 0.1;
        // AccountingApp.expenseRate = 0.3;
        // AccountingApp.print();
        // 만약 다른 취지의 변수 또는 메소드가 필요할 경우,
        // 생산성을 떨어뜨릴 수 있을 수 있으므로 클래스를 도입한다.
        AccountingApp a1 =  new AccountingApp();
        a1.valueOfSupply = 10000.0;
        a1.VATRate = 0.1;
        a1.expenseRate = 0.3;
        a1.print();

        AccountingApp a2 = new AccountingApp();
        a2.valueOfSupply = 200000.0;
        a2.VATRate = 0.05;
        a2.expenseRate = 0.2;
        a2.print();


    }
}


// 인스턴스: 하나의 클래스를 복제해서 서로 다른 데이터의 값과 
// 서로 같은 메소드를 가진 복제본을 만드는 것
// static: https://wikidocs.net/228