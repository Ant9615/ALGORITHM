package myApp;

public class AccountingArray {
    public static void main(String[] args) { 
        double valueOfSupply = Double.parseDouble(args[0]); 
        double VATRate = 0.1;
        double expenseRate = 0.3;
        double VAT = valueOfSupply * VATRate;
        double total = valueOfSupply + VAT;
        double expense = valueOfSupply * expenseRate;
        double income = valueOfSupply - expense;

        double[] DividendRates = new double[3];
        DividendRates[0] = 0.5;
        DividendRates[1] = 0.3;
        DividendRates[2] = 0.2;

        double Dividend_1 = income*DividendRates[0];
        double Dividend_2 = income*DividendRates[1];
        double Dividend_3 = income*DividendRates[2];

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
