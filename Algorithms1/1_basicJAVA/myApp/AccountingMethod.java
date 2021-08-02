package myApp;

public class AccountingMethod {
    // global variable
    public static double valueOfSupply;
    public static double VATRate;
    public static double expenseRate;
    public static void main(String[] args) {
        valueOfSupply = 10000.0;
        VATRate = 0.1;
        expenseRate = 0.3;

        print();

        
    }

    public static double getVAT(){
        return valueOfSupply * VATRate;
    } // 메소드

    public static double getTotal(){
        return valueOfSupply + getVAT();
    }

    public static double getExpense(){
        return valueOfSupply * expenseRate;
    }

    public static double getIncome(){
        return valueOfSupply - getExpense();
    }

    public static double getDividend_1(){
        return getIncome() * 0.5;
    }

    public static double getDividend_2(){
        return getIncome() * 0.3;
    }

    public static double getDividend_3(){
        return getIncome() * 0.2;
    }

    public static void print(){
        System.out.println("Value of Supply: "+ valueOfSupply);
        System.out.println("VAT: "+getVAT());
        System.out.println("Total: "+getTotal());
        System.out.println("Expense: "+getExpense());
        System.out.println("Income: "+getIncome());
        System.out.println("Dividend_1: "+getDividend_1());
        System.out.println("Dividend_2: "+getDividend_2());
        System.out.println("Dividend_3: "+getDividend_3());
    }
}
