package com.example.creditfrauddetection;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

import com.basgeekball.awesomevalidation.AwesomeValidation;
import com.basgeekball.awesomevalidation.ValidationStyle;
import com.google.common.collect.Range;
public class FormPage extends AppCompatActivity {
    EditText etAge,etJob,etCredit,etDuration;
    RadioGroup rgGender,rgHousing,rgSavingAccount,rgCheckingAccount,rgPurpose;

    //defining AwesomeValidation object
    AwesomeValidation awesomeValidation;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_form_page);

        awesomeValidation = new AwesomeValidation(ValidationStyle.BASIC);

        //Assign Edit Text variable
        etAge=findViewById(R.id.et_age);
        etJob=findViewById(R.id.et_Job);
        etCredit=findViewById(R.id.et_creditamount);
        etDuration=findViewById(R.id.et_duration);


        //Initializing radiresGenerato group variables
        rgGender= (RadioGroup) findViewById(R.id.rg_gender);
        rgHousing= (RadioGroup) findViewById(R.id.rg_housing);
        rgSavingAccount= (RadioGroup) findViewById(R.id.rg_savingaccount);
        rgCheckingAccount= (RadioGroup) findViewById(R.id.rg_checkingaccount);
        rgPurpose= (RadioGroup) findViewById(R.id.rg_purpose);

    }

    public void MoveResult(View view) {

        //adding required for radio buttons
        int Gender = rgGender.getCheckedRadioButtonId();
        RadioButton rdGender = findViewById(Gender);

        int Housing = rgHousing.getCheckedRadioButtonId();
        RadioButton rdHousing = findViewById(Housing);

        int SavingAccount = rgSavingAccount.getCheckedRadioButtonId();
        RadioButton rdSA = findViewById(SavingAccount);

        int CheckingAccount = rgCheckingAccount.getCheckedRadioButtonId();
        RadioButton rdCA = findViewById(CheckingAccount);

        int Purpose = rgPurpose.getCheckedRadioButtonId();
        RadioButton rdPurpose = findViewById(Purpose);

        //adding validation to edittexts
        awesomeValidation.addValidation(this, R.id.et_age, Range.closed(19, 75), R.string.ageerror);
        if (Gender == -1){
            Toast.makeText(FormPage.this, "Please give Gender", Toast.LENGTH_SHORT).show();
        }else{
            String Genderstr=rdGender.getText().toString();
        }
        //For job edit text
        awesomeValidation.addValidation(this, R.id.et_Job, Range.closed(0, 3), R.string.joberror);
        //for housing
        if (Housing == -1){
            Toast.makeText(FormPage.this, "Please give type of housing", Toast.LENGTH_SHORT).show();
        }else{
            String Housingstr=rdHousing.getText().toString();
        }
        //for saving account
        if (SavingAccount == -1){
            Toast.makeText(FormPage.this, "Please give Saving Accounts ", Toast.LENGTH_SHORT).show();
        }else{
            String SAstr=rdSA.getText().toString();
        }
        //for checking account
        if (CheckingAccount == -1){
            Toast.makeText(FormPage.this, "Please give Checking account", Toast.LENGTH_SHORT).show();
        }else{
            String CAstr=rdCA.getText().toString();
        }
        //credit amount
        awesomeValidation.addValidation(this, R.id.et_creditamount, Range.closed(250, 18424), R.string.ageerror);
        //duration
        awesomeValidation.addValidation(this, R.id.et_duration, Range.closed(4, 72), R.string.ageerror);
        //purpose
        if (Purpose == -1){
            Toast.makeText(FormPage.this, "Please give the type of purpose", Toast.LENGTH_SHORT).show();
        }else{
            String Purposestr=rdPurpose.getText().toString();
        }


        //Checking radio attributes checked or not
        if (awesomeValidation.validate()) {
            Intent i=new Intent(FormPage.this,ResPage.class);

            startActivity(i);
        }
    }
}