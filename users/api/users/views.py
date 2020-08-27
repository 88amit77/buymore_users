import json
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department, Import, Export
from .serializers import (
	UserSerializer,
	GroupSerializer,
	ContentTypeSerializer,
	PermissionSerializer,
	DepartmentSerializer,
	ImportSerializer,
	ListImportSerializer,
	ExportSerializer,
	ListExportSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]


class ContentTypeViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows contenttypes to be viewed or edited.
	"""
	queryset = ContentType.objects.all()
	serializer_class = ContentTypeSerializer
	permission_classes = [permissions.IsAuthenticated]


class PermissionViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows permissions to be viewed or edited.
	"""
	queryset = Permission.objects.all()
	serializer_class = PermissionSerializer
	permission_classes = [permissions.IsAuthenticated]


class UsernameFilterView(APIView):
	"""
	View to list all users in the system.

	* Requires token authentication.
	* Only admin users are able to access this view.
	"""
	# authentication_classes = [authentication.TokenAuthentication]
	# permission_classes = [permissions.IsAdminUser]

	def get(self, request, format=None):
		"""
		Return a list of all users.
		"""
		qs = User.objects.all().order_by('username')
		if 'id' in request.data:
			ids = request.data['id'].split(',')
			qs = qs.filter(id__in=ids)
		if 'username' in request.data:
			qs = qs.filter(username__contains=request.data['username'])
		usernames = [{user.username: user.username} for user in qs]
		return Response(usernames)


class EmailFilterView(APIView):
	"""
	View to list all users in the system.

	* Requires token authentication.
	* Only admin users are able to access this view.
	"""
	# authentication_classes = [authentication.TokenAuthentication]
	# permission_classes = [permissions.IsAdminUser]

	def get(self, request, format=None):
		"""
		Return a list of all users.
		"""
		qs = User.objects.all().order_by('email')
		if 'id' in request.data:
			ids = request.data['id'].split(',')
			qs = qs.filter(id__in=ids)
		if 'email' in request.data:
			qs = qs.filter(email__contains=request.data['email'])
		email = [{user.email: user.email} for user in qs]
		return Response(email)


class UserIdFilterView(APIView):
	"""
	View to list all users in the system.

	* Requires token authentication.
	* Only admin users are able to access this view.
	"""
	# authentication_classes = [authentication.TokenAuthentication]
	# permission_classes = [permissions.IsAdminUser]

	def get(self, request, format=None):
		"""
		Return a list of all users.
		"""
		qs = User.objects.all().order_by('id')
		if 'id' in request.data:
			ids = request.data['id'].split(',')
			qs = qs.filter(id__in=ids)
		if 'user_id' in request.data:
			user_ids = request.data['user_id'].split(',')
			qs = qs.filter(id__in=user_ids)
		if 'username' in request.data:
			user_names = request.data['username'].split(',')
			qs = qs.filter(username__in=user_names)
		if 'email' in request.data:
			emails = request.data['email'].split(',')
			qs = qs.filter(email__in=emails)

		users = [{user.id: user.id} for user in qs]
		return Response(users)


class UserIdKeywordFilterView(APIView):
	"""
	View to list all users in the system.

	* Requires token authentication.
	* Only admin users are able to access this view.
	"""
	# authentication_classes = [authentication.TokenAuthentication]
	# permission_classes = [permissions.IsAdminUser]

	def get(self, request, format=None):
		"""
		Return a list of all users.
		"""
		qs = User.objects.all().order_by('id')
		if 'id' in request.data:
			ids = request.data['id'].split(',')
			qs = qs.filter(id__in=ids)
		if 'keyword' in request.data:
			qs = qs.filter(email__contains=request.data['keyword']) | qs.filter(username__contains=request.data['keyword']) | qs.filter(id__contains=request.data['keyword'])
		users = [{user.id: user.id} for user in qs]
		return Response(users)


class UserIdDataKeywordFilterView(APIView):
	"""
	View to list all users in the system.

	* Requires token authentication.
	* Only admin users are able to access this view.
	"""
	# authentication_classes = [authentication.TokenAuthentication]
	# permission_classes = [permissions.IsAdminUser]

	def get(self, request, format=None):
		"""
		Return a list of all users.
		"""
		qs = User.objects.all().order_by('id')
		if 'id' in request.data:
			ids = request.data['id'].split(',')
			qs = qs.filter(id__in=ids)
		if 'keyword' in request.data:
			qs = qs.filter(username__contains=request.data['keyword']) | qs.filter(id__contains=request.data['keyword'])
		users = [{user.id: user.id} for user in qs]
		return Response(users)


class UserNameDataKeywordFilterView(APIView):
	"""
	View to list all users in the system.

	* Requires token authentication.
	* Only admin users are able to access this view.
	"""
	# authentication_classes = [authentication.TokenAuthentication]
	# permission_classes = [permissions.IsAdminUser]

	def get(self, request, format=None):
		"""
		Return a list of all users.
		"""
		qs = User.objects.all().order_by('id')
		if 'id' in request.data:
			ids = request.data['id'].split(',')
			qs = qs.filter(id__in=ids)
		if 'keyword' in request.data:
			qs = qs.filter(username__contains=request.data['keyword'])
		users = [{user.id: user.id} for user in qs]
		return Response(users)


class DepartmentViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	permission_classes = [permissions.IsAuthenticated]


class VendorRolesApi(APIView):
	def get(self, request):
		vendor_department = Department.objects.get(pk=2)
		qs = vendor_department.groups.all()
		data = {}
		for group in qs:
			group_id = group.id
			name = group.name
			data[group_id] = name
		return Response(data)


class MarketingInchargeFieldApi(APIView):
	def get(self, request):
		users = User.objects.all()
		data = {}
		for user in users:
			user_id = user.id
			if user.first_name is not '' and user.first_name is not None:
				name = user.first_name
				if user.last_name is not None and user.last_name is not '':
					name = name + ' ' + user.last_name
			else:
				name = user.username
			data[user_id] = name
		return Response(data)


class BrandAnalystFieldApi(APIView):
	def get(self, request):
		users = User.objects.all()
		data = {}
		for user in users:
			user_id = user.id
			if user.first_name is not '' and user.first_name is not None:
				name = user.first_name
				if user.last_name is not None and user.last_name is not '':
					name = name + ' ' + user.last_name
			else:
				name = user.username
			data[user_id] = name
		return Response(data)


class CheckUsernameView(APIView):
	def get(self, request):
		user = User.objects.filter(username=request.data['username'])
		if len(user) > 0:
			return Response({"status": True})
		else:
			return Response({"status": False})


class CheckEmailView(APIView):
	def get(self, request):
		user = User.objects.filter(email=request.data['email'])
		if len(user) > 0:
			return Response({"status": True})
		else:
			return Response({"status": False})

#for import and export api
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

DEFAULT_PAGE = 1
class CustomImportPagination(PageNumberPagination):
	page = DEFAULT_PAGE
	page_size = 20
	page_size_query_param = 'page_size'

	def get_paginated_response(self, data):
		return Response({
			'links': {
				'next': self.get_next_link(),
				'previous': self.get_previous_link()
			},
			'total': self.page.paginator.count,
			'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
			'page_size': int(self.request.GET.get('page_size', self.page_size)),
			'UI_data': {
				'sticky_headers': [
					'user_id',
					'imfile_name',
				],
				'header': {

					'user_id':'User Name',
					'imfile_name':'File Name',
					'imfile_type':'File Type',
					'imfile_size':'File Size',
					'imfile_isread': 'Is Read',
					'imfile_iscompleted': 'Is Completed',
					'created_date':'Created At',
					'updated_date':'Updated At',

				   },
				'sortable': [
					'user_id',
					'imfile_name',
				],
				'searchable': [
					'user_id',
					'imfile_name',
					'imfile_type',
					'imfile_size',
					'imfile_isread',
					'imfile_iscompleted',
					'created_date',
					'updated_date',

				],

			},
			'results': data
		})

class CustomExportPagination(PageNumberPagination):
	page = DEFAULT_PAGE
	page_size = 20
	page_size_query_param = 'page_size'

	def get_paginated_response(self, data):
		return Response({
			'links': {
				'next': self.get_next_link(),
				'previous': self.get_previous_link()
			},
			'total': self.page.paginator.count,
			'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
			'page_size': int(self.request.GET.get('page_size', self.page_size)),
			'UI_data': {
				'sticky_headers': [
					'user_id',
					'exfile_name',
				],
				'header': {

					'user_id':'User Name',
					'exfile_name':'File Name',
					'file_type':'File Type',
					'exfile_size':'File Size',
					'exfile_iscreated': 'Is Read',
					'exfile_isdownloaded': 'Is Downloaded',
					'created_date':'Created At',
					'updated_date':'Updated At',

				   },
				'sortable': [
					'user_id',
					'exfile_name',
				],
				'searchable': [
					'user_id',
					'exfile_name',
					'exfile_type',
					'exfile_size',
					'exfile_iscreated',
					'exfile_isdownloaded',
					'created_date',
					'updated_date',

				],

			},
			'results': data
		})

class ImportViewSet(viewsets.ModelViewSet):

	queryset = Import.objects.all()
	serializer_class = ImportSerializer
	# permission_classes = [permissions.IsAuthenticated]

class ListImportViewSet(viewsets.ViewSet):
	# pagination_class = CustomPagination
	def create(self, request):
		queryset = Import.objects.all()
		serializer = ListImportSerializer(queryset, many=True)
		if len(queryset) > 0:
			paginator = CustomImportPagination()
			result_page = paginator.paginate_queryset(queryset, request)
			serializer = ListImportSerializer(result_page, many=True)
			return paginator.get_paginated_response(serializer.data)
		else:
			paginator = CustomImportPagination()
			result_page = paginator.paginate_queryset(queryset, request)
			return paginator.get_paginated_response(result_page)

class SearchImportViewSet(viewsets.ModelViewSet):
	search_fields = [

		'user_id',
		'imfile_name',
		'imfile_type',
		'imfile_size',
		'imfile_isread',
		'imfile_iscompleted',
		'created_date',
		'updated_date',

	]
	ordering_fields = ['user_id', 'imfile_name',]
	filter_backends = (filters.SearchFilter, filters.OrderingFilter)
	queryset = Import.objects.all()
	serializer_class = ListImportSerializer
	pagination_class = CustomImportPagination


class ExportViewSet(viewsets.ModelViewSet):

	queryset = Export.objects.all()
	serializer_class = ExportSerializer
	# permission_classes = [permissions.IsAuthenticated]


class ListExportViewSet(viewsets.ViewSet):
	# pagination_class = CustomPagination
	def create(self, request):
		queryset = Export.objects.all()
		serializer = ListExportSerializer(queryset, many=True)
		if len(queryset) > 0:
			paginator = CustomExportPagination()
			result_page = paginator.paginate_queryset(queryset, request)
			serializer = ListExportSerializer(result_page, many=True)
			return paginator.get_paginated_response(serializer.data)
		else:
			paginator = CustomExportPagination()
			result_page = paginator.paginate_queryset(queryset, request)
			return paginator.get_paginated_response(result_page)

class SearchExportViewSet(viewsets.ModelViewSet):
	search_fields = [
		'user_id',
		'exfile_name',
		'exfile_size',
		'file_type',
		'exfile_iscreated',
		'exfile_isdownloaded',
		'created_date',
		'updated_date',
					]
	ordering_fields = ['user_id', 'exfile_name','created_date','updated_date']
	filter_backends = (filters.SearchFilter, filters.OrderingFilter)
	queryset = Export.objects.all()
	serializer_class = ListExportSerializer
	pagination_class = CustomExportPagination

class GetCSVHeaders(APIView):
	"""
	GET CSV headers
	"""

	def get(self, request, *args, **kwargs):
		"""
		return csv headers
		"""

		imfile_section = self.request.query_params.get('imfile_section')
		imfile_subsection = self.request.query_params.get('imfile_subsection')

		#### Products
		hsn_csv = ["hsn_code", "max_rate", "min_rate", "threshold_amount", "depend_price", "category_id", "created_at",	"updated_at"]
		price_csv = ["price_rule_code", "percentage_value", "price_rule_type", "list_value","percentage_price_list", "user_type", "description", "created_at", "updated_at"]
		
		master_pdt_csv = ["buymore_sku", "ean", "product_name", "product_mrp", "product_length", "product_breath", "product_width", "product_weight", "min_payout_value", "max_payout_value", "product_model_no", "series_name", "child_variations", "description", "sales_rank", "image_url", "key_point", "status", "brand_id_id", "category_id_id", "hsn_code_id_id", "currency_id_id", "created_at", "updated_at"]

		amazon_pdt_csv = ["product_id","amazon_portal_sku","amazon_unique_id","amazon_listing_id","amazon_price_rule","amazon_break_even_sp","amazon_min_break_even_sp","amazon_max_break_even_sp","amazon_vendors_price","amazon_purchase_order_value","amazon_current_selling_price","amazon_upload_selling_price","amazon_competitor_lowest_price","amazon_account_id","amazon_all_values_external_api","amazon_created_at","amazon_updated_at","amazon_portal_category_id"]

		flipkart_pdt_csv =["product_id","flipkart_portal_sku","flipkart_portal_unique_id","flipkart_listing_id","flipkart_price_rule","flipkart_break_even_sp","flipkart_min_break_even_sp","flipkart_max_break_even_sp","flipkart_vendors_price","flipkart_purchase_order_value","flipkart_current_selling_price","flipkart_upload_selling_price","flipkart_competitor_lowest_price","flipkart_account_id","flipkart_all_values_external_api","flipkart_portal_category_id"]

		paytm_pdt_csv = ["product_id","paytm_portal_sku","paytm_portal_unique_id","paytm_listing_id","paytm_price_rule","paytm_break_even_sp","paytm_min_break_even_sp","paytm_max_break_even_sp","paytm_vendors_price","paytm_purchase_order_value","paytm_current_selling_price","paytm_upload_selling_price","paytm_competitor_lowest_price","paytm_account_id","paytm_all_values_external_api","paytm_portal_category_id"]

		snapdeal_pdt_csv = ["product_id","snapdealp_portal_sku","snapdealp_portal_unique_id","snapdealp_listing_id","snapdealp_price_rule","snapdealp_break_even_sp","snapdealp_min_break_even_sp","snapdealp_max_break_even_sp","snapdealp_vendors_price","snapdealp_purchase_order_value","snapdealp_current_selling_price","snapdealp_upload_selling_price","snapdealp_competitor_lowest_price","snapdealp_account_id","snapdealp_all_values_external_api","snapdealp_portal_category_id"]

		catreq_csv = ["category_name", "default_commission_rate", "a", "b", "c", "d", "max", "min", "created_at", "updated_at"]
		
		pdt_attrib_csv = ["product_id_id","asin", "brand", "name", "item_height", "item_length", "item_width",	"item_weight", "label",	"manufacturers", "model", "package_height", "package_length", "package_width",	"package_weight", "package_quantity", "part_number", "product_group", "product_type_name", "publisher",	"image_url", "image_height", "image_width", "studio", "title", "number_of_images", "image_1", "image_2", "image_3", "image_4", "image_5", "image_6", "number_of_key_points", "key_point_1", "key_point_2", "key_point_3", "key_point_4", "key_point_5", "key_point_6", "browse_node", "selling_price", "mrp", "product_rating", "customer_review", "buy_box_seller_name","buy_box_seller_rating", "description", "multiple_portal_id", "sales_rank", "sales_rank_category",	"seller_name", "created_at", "updated_at"]
		#######################
		
		##### Vendors
		
		vendors_csv = ["user_id", "vendor_name", "vendor_code", "vendor_status", "address", "city", "state", "profile_image", "pincode", "mobile", "optional_phone", "country", "currency_id", "marketing_incharge_id", "brand_coordinators_id", "tds_applicable", "pan", "state_pan", "gst_input", "portal_accepted_for_listing", "vendor_type", "bank_name", "account_number", "ifsc_code", "created_at", "updated_at"]
		
		vendors_contact_csv = ["vendor_id", "email_id", "mobile_number", "name_emp", "designation_emp", "created_at", "modified_at"]
		########################

		######## Orders
		dispatch_csv = ["dd_id_id", "name", "address", "pincode", "location_latitude", "location_longitude",	"email_id", "phone", "status", "l_b_h_w", "bin_id", "picklist_id", "is_mark_placed", "have_invoice_file", "packing_status", "is_dispatch", "dispatch_confirmed", "mf_id_id", "is_shipment_create", "awb", "courier_partner", "shipment_id", "is_canceled", "cancel_inward_bin","created_at", "update_at"]
		
		manifest_csv = ["courier_partner", "mf_sheet", "created_date"]
		
		pod_csv = ["pod_number", "courier_partner_name", "pod_image_list", "total_quantity_received","processed_quantity", "warehouse_id", "courier_received_date",	"created_by", "status", "updated_at"]
		
		refund_csv = ["dd_id_id", "image_list", "return_category", "return_notes", "tracking_id",	"created_at", "updated_at", "processing_date", "return_type", "package_condition",	"is_barcode_required"	"product_condition"	"image_correctness"	"size_correctness","alternate_product_id", "sellable", "pod_id_id"]
		
		reimburse_csv = ["dd_id_id", "case_id", "status_of_case", "case_content", "case_reply","reimbursement_amount"]
		
		new_order_csv = ["dd_id", "product_id", "order_id", "order_item_id", "order_date", "dispatch_by_date",	"portal_id", "portal_sku", "qty", "selling_price", "mrp", "tax_rate", "warehouse_id", "region", "payment_method"]
		
		testnames_csv = ["tn_name", "average_time", "tn_cron_code", "tn_type"]
		
		fulfill_csv = ["dd_id_id", "return_request_date", "actual_return_date", "destination_warehouse_id","return_reason", "sub_reason", "awb", "pod_id_id", "return_type"]

		########################

		##### Employee
		emp_att_csv = ["ar_name", "ar_description", "in_time", "in_grace_mins", "out_time", "out_grace_mins"	"work_duration", "random_weekly_off", "sunday_off", "saturday_sunday_off"]
		
		edu_csv = ["institute_name", "course_type", "Stream", "start_date", "end_date", "average_marks","verified", "educations_id"]
		
		mon_sal_csv = ["emp_id_id", "month", "lop", "no_of_days", "ctc", "basic", "hra", "conveyance_allowances", "medical_allowance", "cca_allowance", "pf_employer", "pf_employee", "pt","esi_employer", "esi_employee",	"net_employee_payable", "due_date", "special_allowances", "over_time","deductions", "reimbursements"]
		
		work_csv = ["company_name", "period_from", "period_to", "designation", "reason_for_leaving", "verified", "work_historys_id"]
		
		emp_csv = ["name", "dob", "gender", "blood_group", "marital_status", "marriage_anniversary","official_email", "personal_email", "official_number", "personal_number", "facebook", "instagram","linkedin", "twitter", "date_of_joining", "probation_period", "current_address_line1", "current_address_line2", "current_country", "current_state", "current_pincode", "current_house_type","current_staying_since", "current_city", "permanent_address_line1", "permanentt_address_line2",	"permanent_country", "permanent_state", "permanent_pincode", "employee_type", "employee_status","job_title", "termination_date", "work_location_add", "designation", "department", "resignation_date","resignation_notes", "notice_date", "notice_period", "bank_acc_number", "ifsc_code", "bank_name"]
		
		leave_csv = ["leave_name", "interval_months", "add_value", "yearly_carry_forward", "document_required"]
		
		fam_csv = ["family_member_name", "relation", "contact_number", "family_members_id"]
		#######################




		if imfile_section == "products":
			
			if imfile_subsection == "hsn":
				csv_headers = hsn_csv
			elif imfile_subsection == "pricerule":
				csv_headers = price_csv
			elif imfile_subsection == "masterproduct":
				csv_headers = master_pdt_csv
			elif imfile_subsection == "productattribute":
				csv_headers = pdt_attrib_csv
			elif imfile_subsection == "catreq":
				csv_headers = catreq_csv
			elif imfile_subsection == "amazonproduct":
				csv_headers = amazon_pdt_csv
			elif imfile_subsection == "flipkartproduct":
				csv_headers = flipkart_pdt_csv
			elif imfile_subsection == "paytmproduct":
				csv_headers = paytm_pdt_csv
			elif imfile_subsection == "snapdealproduct":
				csv_headers = snapdeal_pdt_csv
			else:
				csv_headers = "Invalid Choice selected!!!"
		
		elif imfile_section == "vendors":
			
			if imfile_subsection == "vendor":
				csv_headers = vendor_csv
			elif imfile_subsection == "vendorcontact":
				csv_headers = vendors_contact_csv
			else:
				csv_headers = "Invalid Choice selected!!!"
		
		elif imfile_section == "orders":
			
			if imfile_subsection == "dispatch":
				csv_headers = dispatch_csv
			elif imfile_subsection == "manifest":
				csv_headers = manifest_csv
			elif imfile_subsection == "pod":
				csv_headers = pod_csv
			elif imfile_subsection == "refund":
				csv_headers = refund_csv
			elif imfile_subsection == "reimburse":
				csv_headers = reimburse_csv
			elif imfile_subsection == "testnames":
				csv_headers = testnames_csv
			elif imfile_subsection == "neworder":
				csv_headers = new_order_csv
			elif imfile_subsection == "fulfill":
				csv_headers = fulfill_csv
			else:
				csv_headers = "Invalid Choice selected!!!"
		
		elif imfile_section == "employee":
			if imfile_subsection == "attendance":
				csv_headers = emp_att_csv
			elif imfile_subsection == "education":
				csv_headers = edu_csv
			elif imfile_subsection == "monthlysal":
				csv_headers = mon_sal_csv
			elif imfile_subsection == "workhistory":
				csv_headers = work_csv
			elif imfile_subsection == "emp":
				csv_headers = emp_csv
			elif imfile_subsection == "leave":
				csv_headers = leave_csv
			elif imfile_subsection == "family":
				csv_headers = fam_csv
			else:
				csv_headers = "Invalid Choice selected!!!!!!!!!"
		
		else:
			csv_headers = "No query parameters passed! Hint: imfile_section, imfile_subsection"
			
		res = csv_headers

		return Response(res, status = status.HTTP_200_OK)