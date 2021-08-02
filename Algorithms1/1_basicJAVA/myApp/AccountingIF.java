package myApp;

public class AccountingIF {
    public static void main(String[] args) { //args 입력값을 입력하는 부분임
        double valueOfSupply = Double.parseDouble(args[0]); 
        double VATRate = 0.1;
        Double VAT = valueOfSupply * VATRate;
        double expenseRate = 0.3;
        double total = valueOfSupply + VAT;
        double expense = valueOfSupply * expenseRate;
        double income = valueOfSupply - expense;
        
        double Dividend_1;
        double Dividend_2;
        double Dividend_3;

        if(income > 10000.0){
            Dividend_1 = income*0.5;
            Dividend_2 = income*0.3;
            Dividend_3 = income*0.2;
        } else{
            Dividend_1 = income*1.0;
            Dividend_2 = income*0;
            Dividend_3 = income*0;
        }
        
        System.out.println("Value of Supply: "+ valueOfSupply);
        System.out.println("VAT: "+VAT);
        System.out.println("Total: "+total);
        System.out.println("Expense: "+expense);
        System.out.println("Income: "+income);
        System.out.println("Dividend_1: "+Dividend_1);
        System.out.println("Dividend_2: "+Dividend_2);
        System.out.println("Dividend_3: "+Dividend_3);

    }
}
