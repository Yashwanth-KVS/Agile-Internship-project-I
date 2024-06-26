import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/sample_data/Credit_card.csv')
df["Annual_income"] = df["Annual_income"].fillna(df["Annual_income"].mean())
df["Type_Occupation"] = df["Type_Occupation"].fillna(df["Type_Occupation"].mode()[0])

df = pd.get_dummies(df, columns=["GENDER", "Car_Owner", "Propert_Owner", "Type_Income", "Marital_status", "Housing_type"])


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[["Annual_income"]] = scaler.fit_transform(df[["Annual_income"]])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop("Ind_ID", axis=1), df["Ind_ID"], test_size=0.2, random_state=42)

plt.hist(df["Annual_income"])
plt.xlabel("Scaled Annual Income")
plt.ylabel("Number of People")
plt.title("Distribution of Scaled Annual Income")
plt.show()


data = pd.read_csv('/content/sample_data/loan_approval_dataset.csv')

data

print(data.columns)

data[' education'] = data[' education'].map({'Graduate': 1, 'Not Graduate': 0})
data[' self_employed'] = data[' self_employed'].map({'Yes': 1, 'No': 0})
data[' loan_status'] = data[' loan_status'].map({'Approved': 1, 'Rejected': 0})

data[' residential_assets_value'] = data[' residential_assets_value'].apply(lambda x: max(x, 0))
data[' commercial_assets_value'] = data[' commercial_assets_value'].apply(lambda x: max(x, 0))
data[' luxury_assets_value'] = data[' luxury_assets_value'].apply(lambda x: max(x, 0))
data[' bank_asset_value'] = data[' bank_asset_value'].apply(lambda x: max(x, 0))

plt.figure(figsize=(16, 8))

# Distribution of loan_amount
plt.subplot(2, 2, 1)
sns.histplot(data[' loan_amount'], kde=True, color='blue')
plt.title('Distribution of Loan Amount')

plt.subplot(2, 2, 2)
sns.histplot(data[' cibil_score'], kde=True, color='green')
plt.title('Distribution of CIBIL Score')

plt.subplot(2, 2, 4)
sns.boxplot(x=' loan_status', y=' loan_amount', hue=' loan_status', data=data, palette='muted', dodge=False)
plt.title('Loan Amount vs Loan Status')

plt.tight_layout()
plt.show()
