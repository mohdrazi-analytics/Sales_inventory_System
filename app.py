import streamlit as st
import pyodbc
import pandas as pd
from datetime import datetime


try:
    conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-L3JF97B\\SQLEXPRESS;"
    "DATABASE=sales;"
    "Trusted_Connection=yes;"
)

    cursor = conn.cursor()

except pyodbc.Error as e:
    st.error(f"Database Connection Failed:\n{e}")
    st.stop()




st.set_page_config(
    page_title="Sales Inventory System",
    page_icon="📦",
    layout="wide"
)



st.title("📊 :rainbow[Sales Management System]")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a Page",
    (
        "🏠 Dashboard",
        "➕ Add Product",
        "📋 View Products",
        "✏️ Update Product",
        "🗑️ Delete Product",
        "🗑️ Clean the Database"
    )
)



# ================= Dashboard =================

if page == "🏠 Dashboard":

    st.header("📊 Dashboard")

    try:

        cursor.execute("""
            SELECT
                ISNULL(SUM(Price * Quantity), 0) AS TotalRevenue,
                COUNT(*) AS TotalOrders,
                ISNULL(SUM(Quantity), 0) AS TotalQuantity
            FROM Products
        """)

        result = cursor.fetchone()

        total_revenue = float(result.TotalRevenue)
        total_orders = result.TotalOrders
        total_quantity = result.TotalQuantity

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "💰 Total Revenue",
                f"₹ {total_revenue:,.2f}"
            )

        with col2:
            st.metric(
                "📦 Total Orders",
                total_orders
            )

        with col3:
            st.metric(
                "🛒 Total Quantity Sold",
                total_quantity
            )

    except pyodbc.Error as e:
        st.error(f"❌ Database Error:\n{e}")





        

# ================= Add Product =================

elif page == "➕ Add Product":

    st.header("➕ Add Product")

    category = st.selectbox(
        "Category",
        [
            "Electronics",
            "Furniture",
            "Clothing",
            "Grocery",
            "Sports",
            "Books",
            "Healthcare",
            "Other"
        ]
    )

    product_name = st.text_input("Product Name")

    price = st.number_input(
        "Price",
        min_value=0.0,
        format="%.2f"
    )

    quantity = st.number_input(
        "Quantity",
        min_value=0,
        step=1
    )

    order_date = st.date_input("Order Date")

    save_button = st.button("💾 Save Product")

    if save_button:

        # Validation
        if product_name.strip() == "":
            st.warning("⚠️ Please enter a product name.")

        else:

            try:

                cursor.execute(
                    """
                    INSERT INTO Products
                    (ProductName, Category, Price, Quantity, OrderDate)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        product_name.strip(),
                        category,
                        float(price),
                        int(quantity),
                        order_date      # Pass the date object directly
                    )
                )

                conn.commit()

                st.success("✅ Product Saved Successfully!")

            except pyodbc.Error as e:
                st.error(f"❌ Database Error:\n{e}")





# ================= View Products =================

elif page == "📋 View Products":

    st.header("📋 View Products")

    try:
        cursor.execute("SELECT * FROM Products")

        products = cursor.fetchall()

        if not products:
            st.info("📭 No products found in the database.")

        else:
            columns = [column[0] for column in cursor.description]

            df = pd.DataFrame.from_records(
                products,
                columns=columns
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.success(f"✅ Total Products: {len(df)}")

    except pyodbc.Error as e:
        st.error(f"❌ Database Error:\n{e}")




# ================= Update Product =================

elif page == "✏️ Update Product":

    st.header("✏️ Update Product")

    product_id = st.number_input(
        "Enter Product ID",
        min_value=1,
        step=1,
        key="update_product_id"
    )

    load_button = st.button("🔍 Load Product")

    # ---------------- Load Product ----------------

    if load_button:

        try:
            cursor.execute(
                "SELECT * FROM Products WHERE ProductID = ?",
                (product_id,)
            )

            product = cursor.fetchone()

            if product:

                st.session_state.loaded = True
                st.session_state.product_id = product_id
                st.session_state.product_name = product.ProductName
                st.session_state.category = product.Category
                st.session_state.price = float(product.Price)
                st.session_state.quantity = int(product.Quantity)
                st.session_state.order_date = product.OrderDate

            else:
                st.session_state.loaded = False
                st.error("❌ Product ID not found.")

        except pyodbc.Error as e:
            st.error(f"❌ Database Error:\n{e}")

    # ---------------- Show Form ----------------

    if st.session_state.get("loaded", False):

        categories = [
            "Electronics",
            "Furniture",
            "Clothing",
            "Grocery",
            "Sports",
            "Books",
            "Healthcare",
            "Other"
        ]

        category = st.selectbox(
            "Category",
            categories,
            index=categories.index(st.session_state.category),
            key="update_category"
        )

        product_name = st.text_input(
            "Product Name",
            value=st.session_state.product_name,
            key="update_name"
        )

        price = st.number_input(
            "Price",
            min_value=0.0,
            value=st.session_state.price,
            format="%.2f",
            key="update_price"
        )

        quantity = st.number_input(
            "Quantity",
            min_value=0,
            value=st.session_state.quantity,
            step=1,
            key="update_quantity"
        )

        order_date = st.date_input(
            "Order Date",
            value=st.session_state.order_date,
            key="update_date"
        )

        update_button = st.button("💾 Update Product")

        if update_button:

            if product_name.strip() == "":
                st.warning("⚠️ Product name cannot be empty.")

            else:

                try:

                    cursor.execute(
                        """
                        UPDATE Products
                        SET ProductName = ?,
                            Category = ?,
                            Price = ?,
                            Quantity = ?,
                            OrderDate = ?
                        WHERE ProductID = ?
                        """,
                        (
                            product_name.strip(),
                            category,
                            float(price),
                            int(quantity),
                            order_date,
                            st.session_state.product_id
                        )
                    )

                    conn.commit()

                    st.success("✅ Product Updated Successfully!")

                except pyodbc.Error as e:
                    st.error(f"❌ Database Error:\n{e}")





# ================= Delete Product =================

elif page == "🗑️ Delete Product":

    st.header("🗑️ Delete Product")

    product_id = st.number_input(
        "Enter Product ID",
        min_value=1,
        step=1,
        key="delete_product"
    )

    delete_button = st.button("🗑️ Delete Product")

    if delete_button:

        try:

            # Check whether the product exists
            cursor.execute(
                "SELECT * FROM Products WHERE ProductID = ?",
                (product_id,)
            )

            product = cursor.fetchone()

            if product is None:

                st.error("❌ Product ID not found.")

            else:

                cursor.execute(
                    "DELETE FROM Products WHERE ProductID = ?",
                    (product_id,)
                )

                conn.commit()

                st.success("✅ Product Deleted Successfully!")

        except pyodbc.Error as e:

            st.error(f"❌ Database Error:\n{e}")




elif page == "🗑️ Clean the Database":
    st.subheader("⚠ Danger Zone")

    confirm = st.checkbox("I understand this will delete all records.")

    if st.button("Delete All Data"):
        if confirm:
           cursor.execute("DELETE FROM Products")
           cursor.execute("DBCC CHECKIDENT ('Products', RESEED, 0)")
           conn.commit()
           st.success("All data deleted successfully!")
        else:
          st.warning("Please confirm before deleting.")
    