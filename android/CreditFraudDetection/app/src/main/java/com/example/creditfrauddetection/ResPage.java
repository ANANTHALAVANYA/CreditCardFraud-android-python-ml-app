package com.example.creditfrauddetection;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class ResPage extends AppCompatActivity {
    TextView tvmsg;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_res_page);

        tvmsg=findViewById(R.id.resMsg);

    }
}