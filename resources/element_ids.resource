*** Settings ***

Documentation    Element ids for the Sample_Android_App_Login_Test interface

*** Variables ***

${Form.Login.EmailAddress.Txt}    id=com.loginmodule.learning:id/textInputEditTextEmail
${Form.Login.Password.Txt}    id=com.loginmodule.learning:id/textInputEditTextPassword
${Form.Login.Login.Btn}    id=com.loginmodule.learning:id/appCompatButtonLogin
${Form.Login.CreateOne.Link}    id=com.loginmodule.learning:id/textViewLinkRegister

${Form.Register.Name.Txt}    xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.support.v7.widget.LinearLayoutCompat/TextInputLayout[1]/android.widget.EditText
#${Form.Register.Name.Txt}    id=com.loginmodule.learning:id/textInputEditTextName
${Form.Register.EmailAddress.Txt}    id=com.loginmodule.learning:id/textInputEditTextEmail
${Form.Register.Password.Txt}    id=com.loginmodule.learning:id/textInputEditTextPassword
${Form.Register.PasswordConfirmation.Txt}    id=com.loginmodule.learning:id/textInputEditTextConfirmPassword
${Form.Register.Register.Btn}    id=com.loginmodule.learning:id/appCompatButtonRegister

${Form.Account.Name.Txt}    xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]
#${Form.Account.Name.Txt}    id=com.loginmodule.learning:id/textViewName
${Form.Account.EmailAddress.Txt}    id=com.loginmodule.learning:id/textViewEmail
${Form.Account.Password.Txt}    id=com.loginmodule.learning:id/textViewPassword    