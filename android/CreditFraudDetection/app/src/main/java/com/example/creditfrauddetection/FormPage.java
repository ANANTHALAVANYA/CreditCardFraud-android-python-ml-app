
package com.example.creditfrauddetection;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import com.basgeekball.awesomevalidation.AwesomeValidation;
import com.basgeekball.awesomevalidation.ValidationStyle;
import com.google.common.collect.Range;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

public class FormPage extends AppCompatActivity implements AdapterView.OnItemSelectedListener {

    EditText etAge,etJob,etCredit,etDuration;
    Spinner spinner1,spinner2,spinner3,spinner4,spinner5,spin;
    Button s;

    AwesomeValidation awesomeValidation;
    String etAgestr,etJobstr,etCreditstr,etDurationstr,Genderstr,Housingstr,SavingAccountstr,CheckingAccountstr,Purposestr;
    //defining AwesomeValidation object
    static int i=0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_form_page);
        etAge=findViewById(R.id.etAge);
        etJob=findViewById(R.id.etJob);
        etCredit=findViewById(R.id.etCredit);
        etDuration=findViewById(R.id.etDuration);
        s=findViewById(R.id.s);
        spinner1=findViewById(R.id.spinner1);
        spinner2=findViewById(R.id.spinner2);
        spinner3=findViewById(R.id.spinner3);
        spinner4=findViewById(R.id.spinner4);
        spinner5=findViewById(R.id.spinner5);
        awesomeValidation = new AwesomeValidation(ValidationStyle.BASIC);

        //Assign Edit Text variable
        /*etAgestr=etAge.getText().toString();
        etJobstr=etJob.getText().toString();
        etCreditstr=etCredit.getText().toString();
        etDurationstr=etDuration.getText().toString();*/

        awesomeValidation = new AwesomeValidation(ValidationStyle.BASIC);
        //Age
        awesomeValidation.addValidation(this, R.id.etAge, Range.closed(19, 75), R.string.ageerror);
        //Job
        awesomeValidation.addValidation(this, R.id.etJob, Range.closed(0, 3), R.string.joberror);
        //creditAmount
        awesomeValidation.addValidation(this, R.id.etCredit, Range.closed(250, 18424), R.string.credit);
        //duration
        awesomeValidation.addValidation(this, R.id.etDuration, Range.closed(4, 72), R.string.duration);



        Spinner dropdown = findViewById(R.id.spinner1);
        String[] items = new String[]{"Male", "Female"};
        Spinner dropdown1 = findViewById(R.id.spinner2);
        String[] items1 = new String[]{"own", "free", "rent"};
        Spinner dropdown2 = findViewById(R.id.spinner3);
        String[] items2 = new String[]{"little", "moderate", "quite rich"};
        Spinner dropdown3= findViewById(R.id.spinner4);
        String[] items3 = new String[]{"little", "moderate", "quite rich"};
        Spinner dropdown4 = findViewById(R.id.spinner5);
        String[] items4 = new String[]{"car", "radio/tv", "business","education","furniture/equipment","repairs","vacation/others","domestic appliances"};

        //creating adapters for spinners
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, items);
        dropdown.setAdapter(adapter);
        ArrayAdapter<String> adapter1 = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, items1);
        dropdown1.setAdapter(adapter1);
        ArrayAdapter<String> adapter2 = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, items2);
        dropdown2.setAdapter(adapter2);
        ArrayAdapter<String> adapter3 = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, items3);
        dropdown3.setAdapter(adapter3);
        ArrayAdapter<String> adapter4 = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, items4);
        dropdown4.setAdapter(adapter4);

        // Spinner click listener
        spinner1.setOnItemSelectedListener(this);
        spinner2.setOnItemSelectedListener(this);
        spinner3.setOnItemSelectedListener(this);
        spinner4.setOnItemSelectedListener(this);
        spinner5.setOnItemSelectedListener(this);




    }
    public void submit(View view) {

        if (awesomeValidation.validate()) {
            if(!TextUtils.isEmpty(etAgestr)&&(!TextUtils.isEmpty(etCreditstr)&&(!TextUtils.isEmpty(etJobstr)&&(!TextUtils.isEmpty(etDurationstr))))) {
                RequestQueue requestQueue = Volley.newRequestQueue(this);
                final String url = "";
                JSONObject postParams = new JSONObject();
                try {
                    postParams.put("Age",etAgestr);
                    postParams.put("Gender", Genderstr);
                    postParams.put("job", etJobstr);
                    postParams.put("housing type",Housingstr);
                    postParams.put("saving account", SavingAccountstr);
                    postParams.put("Checking account", CheckingAccountstr);
                    postParams.put("Credit amount", etCreditstr);
                    postParams.put("Duration",etDurationstr);
                    postParams.put("Purpose type", Purposestr);
                }
                catch (JSONException e)
                {
                    e.printStackTrace();
                }

                JsonObjectRequest jsonObjectRequest=new JsonObjectRequest(Request.Method.POST, url, postParams, new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {


                        Log.i("On Response", "onResponse: " + response.toString());
                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.i("On Error",error.toString());
                        Toast.makeText(FormPage.this, ""+error.toString(), Toast.LENGTH_SHORT).show();
                    }
                });
                requestQueue.add(jsonObjectRequest);

            }

            Intent i=new Intent(FormPage.this,ResPage.class);


            startActivity(i);
        }
    }


    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        String item = parent.getItemAtPosition(position).toString();
        i=i+1;
        if(i==1){
            Genderstr=item;}
        if(i==2){
            Housingstr=item;}
        if(i==3){
            SavingAccountstr=item;}
        if(i==4){
            CheckingAccountstr=item;}
        if(i==5){
            Purposestr=item;}

        // Showing selected spinner item
        Toast.makeText(parent.getContext(), "Selected: " + item, Toast.LENGTH_LONG).show();
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }
}