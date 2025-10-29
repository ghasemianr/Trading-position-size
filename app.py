import streamlit as st

def calculate_position_size(account_balance, entry_price, stop_loss_price, risk_percentage):
    """
    محاسبه حجم پوزیشن تریدینگ
    
    ورودی‌ها:
    - account_balance: میزان حساب (مثلا 1000)
    - entry_price: قیمت ورود (مثلا 100)
    - stop_loss_price: قیمت استاپ لاس (مثلا 95)
    - risk_percentage: درصد ریسک (مثلا 1 برای 1%)
    
    خروجی: سایز پوزیشن (تعداد واحد)
    """
    
    # بررسی ورودی‌ها
    if account_balance <= 0 or risk_percentage <= 0:
        raise ValueError("میزان حساب و درصد ریسک باید مثبت باشند!")
    
    if entry_price == stop_loss_price:
        raise ValueError("قیمت ورود و استاپ لاس نمی‌توانند برابر باشند!")
    
    # محاسبه
    risk_amount = (account_balance * risk_percentage) / 100
    price_difference = abs(entry_price - stop_loss_price)
    position_size = risk_amount / price_difference
    
    return position_size

# رابط وب با Streamlit
st.title("🎯 محاسب‌کننده حجم پوزیشن تریدینگ")
st.markdown("ورودی‌ها رو وارد کن و دکمه محاسبه رو بزن!")

# ورودی‌ها
account_balance = st.number_input("💰 میزان حساب (دلار):", min_value=0.0, value=1000.0, step=1.0)
entry_price = st.number_input("📈 قیمت ورود:", min_value=0.0, value=100.0, step=0.01)
stop_loss_price = st.number_input("📉 قیمت استاپ لاس:", min_value=0.0, value=95.0, step=0.01)
risk_percentage = st.number_input("⚠️ درصد ریسک (مثلا 1 برای 1%):", min_value=0.0, value=1.0, step=0.1)

# دکمه محاسبه
if st.button("محاسبه حجم پوزیشن"):
    try:
        position_size = calculate_position_size(account_balance, entry_price, stop_loss_price, risk_percentage)
        risk_amount = (account_balance * risk_percentage) / 100
        st.success(f"✅ سایز پوزیشن (حجم پوزیشن): {position_size:.4f} واحد")
        st.info(f"💡 یادآوری: اگر استاپ بخوره، ضرر شما {risk_amount:.2f} دلار می‌شه.")
    except ValueError as e:
        st.error(f"❌ خطا: {e}")

# توضیح کوتاه
st.markdown("---")
st.markdown("**نحوه کار:** این اپ ریسک‌مدیریت استاندارد رو اعمال می‌کنه. سایز پوزیشن = (حساب × درصد ریسک ÷ 100) ÷ |قیمت ورود - استاپ لاس|")